import contextlib
import io
import json
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

import ingest
from courses import ensure_meta, source_course, course_context
from document_sources import source_metadata, storage_stem
from search import filter_mask


class EngineeringImportTests(unittest.TestCase):
    def test_year_semester_and_track_are_taken_from_folders(self):
        samples = {
            'ING 1/S1 GM /PROBA/Cours/CM.pdf': ('ing-1-s1-gm-probabilites', 1, 1, 'gm'),
            'ING 1/S1 INFO/Proba-DS/DS.pdf': ('ing-1-s1-info-probabilites', 1, 1, 'info'),
            'ING 1/S2 DATA/Système d_exploitation/TD/TD1.pdf': ('ing-1-s2-data-systeme-exploitation', 1, 2, 'data'),
            'ING 2/Semestre 1/Modèle linéaire bis/CM.pdf': ('ing-2-s1-modele-lineaire', 2, 1, None),
            'ING 2/Semestre 2/EDP/TD1.pdf': ('ing-2-s2-edp', 2, 2, None),
            'ING 2/Semestre 2/Methodes Agile_v1.pdf': ('ing-2-s2-methodes-agiles', 2, 2, None),
            'ING 1/Rentrée ING1 FISE.pdf': ('ing-1-informations', 1, None, None),
            'ING 1/S1 GM /EXAMEN/Fiche de revision ALGO.pdf': ('ing-1-s1-gm-algorithmique', 1, 1, 'gm'),
        }
        for path, (course, year, semester, track) in samples.items():
            with self.subTest(path=path):
                self.assertEqual(source_course(path), course)
                meta = ensure_meta({'course': course})
                self.assertEqual((meta['program'], meta['study_year'], meta['semester'], meta['track']), ('ing', year, semester, track))
        self.assertIsNone(source_course('ING 1/S1 INCONNU/Proba/CM.pdf'))

    def test_filters_never_confuse_ing_with_preing_or_other_tracks(self):
        courses = ['analyse1', 'ing-1-s1-gm-probabilites', 'ing-1-s1-info-probabilites', 'ing-2-s1-modele-lineaire', 'ing-1-informations']
        chunks = [ingest.parse_meta('TD1_2024-2025', c) for c in courses]
        mask = filter_mask(chunks, programs={'ing'}, study_years={1}, semesters={1}, tracks={'gm'}, years={2024})
        self.assertEqual(mask.tolist(), [False, True, False, False, False])
        self.assertFalse(filter_mask(chunks, programs={'preing'}, courses={'ing-1-s1-gm-probabilites'}).any())
        self.assertEqual(filter_mask(chunks, programs={'ing'}, semesters={'none'}).tolist(), [False, False, False, False, True])
        self.assertEqual(filter_mask(chunks, programs={'preing'}, study_years={1}).tolist(), [True, False, False, False, False])

    def test_metadata_does_not_label_mixed_exam_folder_as_all_corrections(self):
        course = 'ing-1-s1-gm-probabilites'
        root = 'ING 1/S1 GM /PROBA/Examens & Correction/'
        meta = source_metadata(root + 'Examen--Probabilite2021-2022.pdf', course)
        self.assertEqual((meta['kind'], meta['year'], meta['corrige']), ('ds', 2021, False))
        meta = source_metadata(root + 'Corrigé Examen 24-25.pdf', course)
        self.assertEqual((meta['year'], meta['corrige']), (2024, True))
        meta = source_metadata('ING 1/S1 GM /EXAMEN/Fiche de revision proba.pdf', course)
        self.assertEqual(meta['kind'], 'cours')
        meta = source_metadata('ING 1/S1 GM /PROBA/Annales/2024.pdf', course)
        self.assertIsNone(meta['year'])
        self.assertEqual(meta['kind'], 'ds')

    def test_duplicate_names_and_tracks_remain_separate_and_repeat_import_is_safe(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            paths = []
            for track, chapter, text in [('GM ', 'Chapitre 1', 'Première méthode de calcul. ' * 12),
                                         ('GM ', 'Chapitre 2', 'Deuxième méthode de calcul. ' * 12),
                                         ('INFO', 'Chapitre 1', 'Première méthode de calcul. ' * 12)]:
                path = root / 'ING 1' / ('S1 ' + track) / 'PROBA' / chapter / 'TD1.txt'
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text)
                paths.append(path)
            with patch.object(ingest, 'DATA_ROOT', str(root / 'data')), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(ingest.cmd_add([str(root / 'ING 1')]), 3)
                for path in paths:
                    course = source_course(path)
                    stem = storage_stem(path, course)
                    chunks = ingest.chunk_document(str(root / 'data' / course / (stem + '.txt')), course)
                    self.assertIn(path.read_text().strip(), chunks[0]['text'])
                    self.assertEqual(chunks[0]['title'], 'TD1')
                    self.assertNotIn(stem, chunks[0]['doc_label'])
                self.assertEqual(ingest.cmd_add([str(root / 'ING 1')]), 0)

    def test_code_is_kept_as_code_without_execution_or_math_reconstruction(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            path = root / 'ING 2' / 'Semestre 2' / 'IA' / 'example.py'
            path.parent.mkdir(parents=True)
            source = "# Do not execute this source\nraise RuntimeError('code must stay inert')\nvalue = '<script>$x$</script>'\n"
            path.write_text(source)
            with patch.object(ingest, 'DATA_ROOT', str(root / 'data')), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(ingest.cmd_add([str(path)]), 1)
                course = source_course(path)
                chunks = ingest.chunk_document(str(root / 'data' / course / (storage_stem(path, course) + '.txt')), course)
                self.assertEqual(chunks[0]['fmt'], 'code')
                self.assertEqual(chunks[0]['kind'], 'ressource')
                self.assertEqual(chunks[0]['text'], source.strip())

    def test_pptx_slide_order_and_excel_shared_strings(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'slides.pptx'
            with zipfile.ZipFile(path, 'w') as archive:
                for n in (10, 2, 1):
                    archive.writestr(f'ppt/slides/slide{n}.xml', f'<root xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:p><a:r><a:t>Diapositive {n}</a:t></a:r></a:p></root>')
            self.assertEqual(ingest.extract_file(path).split(ingest.PAGE_SEP), ['Diapositive 1', 'Diapositive 2', 'Diapositive 10'])
            path = Path(folder) / 'data.xlsx'
            ns = 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'
            with zipfile.ZipFile(path, 'w') as archive:
                archive.writestr('xl/workbook.xml', f'<workbook xmlns="{ns}" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets><sheet name="Budget" r:id="rId1"/></sheets></workbook>')
                archive.writestr('xl/_rels/workbook.xml.rels', '<Relationships><Relationship Id="rId1" Target="worksheets/sheet1.xml"/></Relationships>')
                archive.writestr('xl/sharedStrings.xml', f'<sst xmlns="{ns}"><si><t>Recettes</t></si></sst>')
                archive.writestr('xl/worksheets/sheet1.xml', f'<worksheet xmlns="{ns}"><sheetData><row><c r="A1" t="s"><v>0</v></c><c r="B1"><v>42</v></c></row></sheetData></worksheet>')
            self.assertEqual(ingest.extract_file(path), 'Budget\nA1: Recettes | B1: 42')

    def test_images_and_unsupported_attachments_are_reported(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / 'ING 2' / 'Semestre 1' / 'Traitement du signal'
            source.mkdir(parents=True)
            (source / 'scan.jpg').write_bytes(b'not plain text')
            (source / 'signal.wav').write_bytes(b'not plain text')
            data = root / 'data'
            data.mkdir()
            with patch.object(ingest, 'DATA_ROOT', str(data)), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(ingest.cmd_add([str(source)]), 0)
                report = json.loads((data / 'import-report.json').read_text())
                self.assertEqual({r['status'] for r in report}, {'à transcrire', 'annexe non indexée'})
