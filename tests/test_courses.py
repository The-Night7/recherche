import tempfile
import unittest
import json
import zipfile
from unittest.mock import patch
from pathlib import Path

import ingest
from courses import COURSES, CURRICULUM, CURRICULA, course_context, detect_course, source_course, ensure_meta
from references import annotate, match, parse_reference
from search import filter_mask


class CourseImportTests(unittest.TestCase):
    def test_all_subject_filename_variants_are_recognized(self):
        samples = {
            'TD01-Listes-Chainee_2024-2025_Informatique3_P2S1_DInformatique': 'informatique3',
            '2024-11-05-DS1-2024-2025-V1-Correction_Informatique3-DS_P2S1_AhmedA': 'informatique3',
            'CM-Chapitre4-Gauss_2024-2025_Electromagnetisme_P2S1_EDupont': 'electromagnetisme',
            'CC2-2023-2024-Correction_Electromagnetisme-CC_P2S1_DPhysique': 'electromagnetisme',
            'CM3-Methodes_2024-2025_SHS_P2S1_DH&D': 'shs',
            'DS120232024V4_SeriesDS_P2S1_DMaths': 'series',
            'DS1-2023-2024_Analyse-dans-RN-DS_P2S1_DMaths': 'analyse-rn',
        }
        for stem, course in samples.items():
            with self.subTest(stem=stem):
                self.assertEqual(detect_course(stem), course)
                meta = ingest.parse_meta(stem, course)
                self.assertEqual(meta['curriculum'], 'preing-2-s1')
                self.assertIsNotNone(meta['year'])
        self.assertIsNone(detect_course('CM_2024-2025_Inconnu_P2S1_Test'))

    def test_legacy_context_and_new_curricula_are_distinct(self):
        self.assertEqual((CURRICULUM['study_year'], CURRICULUM['semester']), (2, 1))
        for course in ('analyse-rn', 'series', 'informatique3', 'electromagnetisme', 'shs'):
            self.assertEqual(ensure_meta({'course': course})['curriculum'], CURRICULUM['id'])
        legacy = ensure_meta({'label': 'TD1 : Normes', 'text': 'Exercice 1'})
        self.assertEqual(legacy['course'], 'analyse-rn')
        self.assertEqual(legacy['curriculum'], CURRICULUM['id'])
        for course in COURSES:
            chunk = ensure_meta({'course': course})
            self.assertEqual((chunk['study_year'], chunk['semester']),
                             (course_context(course)['study_year'], course_context(course)['semester']))
        self.assertEqual(len([c for c in CURRICULA.values() if c['program'] == 'preing']), 4)

    def test_folder_context_disambiguates_projects_and_corrects_mislabeled_filename(self):
        for semester in (1, 2):
            filename = f'TD1_2024-2025_Projet1_P1S{semester}_DProjet'
            self.assertEqual(detect_course(filename), f'projet1-s{semester}')
        source = 'PREING1-S2/Mecanique-du-point/2024-02-01-CM_2023-2024_Mecanique-du-point_P2S1_FPiguet.md'
        self.assertEqual(source_course(source), 'mecanique-du-point')
        self.assertEqual(ingest.parse_meta(Path(source).stem, source_course(source))['curriculum'], 'preing-1-s2')
        self.assertIsNone(detect_course('CM_2024-2025_Analyse1_P2S2_DMaths'))
        self.assertEqual(source_course('PREING2-S2/Fiche de Révision Algèbre.docx'), 'algebre-lineaire')
        self.assertEqual(source_course('PREING2-S2/Physique-moderne-PROJET/exemple1.pdf'), 'physique-moderne')

    def test_study_year_semester_and_academic_year_filters_intersect(self):
        chunks = [ingest.parse_meta('TD1_2024-2025', c) for c in
                  ('analyse1', 'analyse2', 'series', 'integration-proba')]
        self.assertEqual(filter_mask(chunks, study_years={1}, semesters={2}, years={2024}).tolist(),
                         [False, True, False, False])
        self.assertFalse(filter_mask(chunks, study_years={1}, semesters={2}, courses={'series'}).any())
        self.assertEqual(filter_mask(chunks, semesters={1}).tolist(), [True, False, True, False])
        self.assertFalse(filter_mask(chunks, study_years={1}, years={2023}).any())

    def test_docx_import_and_projects_survive_a_rebuild_without_cross_semester_deduplication(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            data = root / 'data'
            inputs = []
            body = ('Préparer la présentation du projet et expliquer la démarche. ' * 8)
            for semester in (1, 2):
                path = root / f'PREING1-S{semester}' / 'Projet1' / 'Projet.docx'
                path.parent.mkdir(parents=True)
                with zipfile.ZipFile(path, 'w') as archive:
                    archive.writestr('word/document.xml', '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body><w:p><w:r><w:t>' + body + '</w:t></w:r></w:p></w:body></w:document>')
                inputs.append(str(path.parent.parent))
            with patch.object(ingest, 'DATA_ROOT', str(data)):
                self.assertEqual(ingest.cmd_add(inputs), 2)
                for semester in (1, 2):
                    course = f'projet1-s{semester}'
                    chunks = ingest.chunk_document(str(data / course / 'Projet.txt'), course)
                    self.assertEqual(chunks[0]['semester'], semester)
                    self.assertEqual(chunks[0]['kind'], 'projet')
                    self.assertIn(body.strip(), chunks[0]['text'])
                self.assertEqual(ingest.cmd_add(inputs), 0)
                self.assertEqual(len(json.loads((data / 'import-report.json').read_text())), 2)

    def test_continuous_assessment_and_resits_are_searchable(self):
        cc = ingest.parse_meta('CC2-2023-2024-Correction_Electromagnetisme-CC_P2S1_DPhysique', 'electromagnetisme')
        self.assertEqual((cc['kind'], cc['title'], cc['corrige']), ('cc', 'CC2', True))
        resit = ingest.parse_meta('Rattrapage-2023-2024-Sujet_Electromagnetisme-CC_P2S1_DPhysique', 'electromagnetisme')
        self.assertEqual((resit['kind'], resit['title'], resit['corrige']), ('cc', 'Rattrapage', False))
        chunk = annotate([dict(cc, label=cc['doc_label'], section='Exercice 1', text='Exercice 1')])[0]
        reference, _ = parse_reference('CC2 corrigé exercice 1')
        self.assertTrue(match(chunk, reference))
        reference, _ = parse_reference('DS2 exercice 1')
        self.assertFalse(match(chunk, reference))
        self.assertTrue(filter_mask([chunk], courses={'electromagnetisme'}, kinds={'cc'})[0])
        self.assertFalse(filter_mask([chunk], courses={'informatique3'})[0])

    def test_code_and_non_math_prose_preserve_their_source(self):
        with tempfile.TemporaryDirectory() as folder:
            code = 'Exercice 1\nvoid empiler(Pile* p) {\n    p->tete = NULL;\n    int n = 2;\n}\n'
            path = Path(folder) / 'TD2_2024-2025_Informatique3_P2S1_DInformatique.txt'
            path.write_text(code)
            chunk, = ingest.chunk_document(str(path), 'informatique3')
            self.assertEqual(chunk['fmt'], 'text')
            self.assertEqual(chunk['text'], code.strip())
            path = Path(folder) / 'CM1_2024-2025_SHS_P2S1_DHD.txt'
            prose = 'La recherche documentaire permet de comparer plusieurs sources et leurs méthodes.'
            path.write_text(prose)
            chunk, = ingest.chunk_document(str(path), 'shs')
            self.assertEqual(chunk['fmt'], 'text')
            self.assertEqual(chunk['text'], prose)

    def test_code_comments_do_not_split_markdown_exercises(self):
        source = '## Exercice 1\n\n```shell\n# Afficher les fichiers\nls -l\n```\n\n## Exercice 2\n\nLa suite.'
        sections = ingest.sections_markdown(source)
        self.assertEqual([label for label, _ in sections], ['Exercice 1', 'Exercice 2'])
        self.assertIn('```shell\n# Afficher les fichiers\nls -l\n```', sections[0][1])


if __name__ == '__main__':
    unittest.main()
