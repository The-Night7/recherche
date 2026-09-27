import tempfile
import unittest
from pathlib import Path

from document_sources import find_source

from ingest import align_legacy, resplit_legacy, strip_page_numbers, superseded_removed
from references import annotate, match, parse_reference


def page(label, text, kind="td", corrige=True):
    return {"label": label, "doc_label": label, "section": "", "text": text, "kind": kind,
            "corrige": corrige, "course": "analyse-rn", "fmt": "pdf"}


class LegacyChunksTests(unittest.TestCase):
    def test_page_numbers_follow_the_numbering(self):
        self.assertEqual(strip_page_numbers(["a\n21", "on a x < r²²", "fin r²"]), ["a", "on a x < r", "fin r²"])
        # 29 égaré au milieu de la page par l'extraction
        self.assertEqual(strip_page_numbers(["a\n28", "b\n29\n8. I", "c\n30"]), ["a", "b\n8. I", "c"])

    def test_pages_are_regrouped_by_exercise(self):
        doc = "TD2 : Ouverts et fermés (ancienne correction, avant réforme)"
        pages = [page(doc, "Exercice 1 : Normes\nSoit E.\nRéponses :\n1. Alors\n21"),
                 page(doc, "(puisque R = r″/α).\nExercice 2 :\nSoit une boule.\n22"),
                 page(doc, "Exercice 3 :\nDéterminer si les ensembles suivants.\n23")]
        chunks = resplit_legacy(pages)
        self.assertEqual([c["section"] for c in chunks], ["Exercice 1", "Exercice 2", "Exercice 3"])
        self.assertTrue(chunks[0]["text"].endswith("(puisque R = r″/α)."))
        self.assertEqual(resplit_legacy(chunks), chunks)

        # L'ancien exercice 3 corrige l'exercice 2 de la feuille 2025-2026 ; l'ancien 1 n'y est plus.
        annotate(align_legacy(chunks))
        ref, _ = parse_reference("td2 exercice 2 corrigé")
        self.assertEqual([c["section"] for c in chunks if match(c, ref)], ["Exercice 3"])
        self.assertIn("= TD2 2025-2026, exercice 2", chunks[2]["label"])
        ref, _ = parse_reference("td2 exercice 1 corrigé")
        self.assertEqual([c["section"] for c in chunks if match(c, ref)], ["Exercice 2"])

    def test_sources_are_found_in_the_course_folder(self):
        with tempfile.TemporaryDirectory() as root:
            pdf = Path(root, "Synthèses de Cours", "PREING2-S1", "Analyse-dans-RN", "TD.pdf")
            pdf.parent.mkdir(parents=True)
            pdf.write_bytes(b"%PDF")
            self.assertEqual(find_source("PREING2-S1/Analyse-dans-RN/TD.pdf", root), str(pdf))
            self.assertIsNone(find_source("PREING2-S1/absent.pdf", root))

    def test_transcribed_exercises_replace_the_old_correction(self):
        old = [{"section": "Exercice 3", "current": {"td": 2, "exercise": 2, "partial": False}},
               {"section": "Exercice 1"}]
        new = [{"doc": "TD2-Correction_2025-2026_Analyse-dans-RN_P2S1_EMasnada", "section": "Exercice 2 : Ouverts"}]
        self.assertEqual(superseded_removed(old, new), [{"section": "Exercice 1"}])


if __name__ == "__main__":
    unittest.main()
