import unittest

from ingest import align_legacy, resplit_legacy, strip_page_numbers
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


if __name__ == "__main__":
    unittest.main()
