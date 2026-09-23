import tempfile
import unittest
from pathlib import Path

import ingest
from courses import COURSES, CURRICULUM, detect_course, ensure_meta
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

    def test_current_and_legacy_content_share_the_study_context(self):
        self.assertEqual((CURRICULUM['study_year'], CURRICULUM['semester']), (2, 1))
        for course in COURSES:
            self.assertEqual(ensure_meta({'course': course})['curriculum'], CURRICULUM['id'])
        legacy = ensure_meta({'label': 'TD1 : Normes', 'text': 'Exercice 1'})
        self.assertEqual(legacy['course'], 'analyse-rn')
        self.assertEqual(legacy['curriculum'], CURRICULUM['id'])

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
