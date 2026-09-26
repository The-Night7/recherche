import unittest

from ingest import fix_accents


class AccentTests(unittest.TestCase):
    def test_recompose_accents_separes(self):
        self.assertEqual(fix_accents("Th´ eorie des probl` emes"), "Théorie des problèmes")
        self.assertEqual(fix_accents("d´ eterminant si une ´ equation"), "déterminant si une équation")
        self.assertEqual(fix_accents("(en 1900 ` a Paris)"), "(en 1900 à Paris)")
        self.assertEqual(fix_accents("Gaspard F´ erey, Mˆ eme, na¨ıve"), "Gaspard Férey, Même, naïve")

    def test_ne_touche_pas_au_reste(self):
        for text in ["f´(x) = 2", "`code` et `x`", "déjà accentué", "a` b"]:
            self.assertEqual(fix_accents(text), text)


if __name__ == "__main__":
    unittest.main()


class SpacingTests(unittest.TestCase):
    def test_variable_collee_au_mot(self):
        from ingest import fix_spacing
        self.assertEqual(fix_spacing("valeurs singulières deA. La matriceA = 1"), "valeurs singulières de A. La matrice A = 1")
        self.assertEqual(fix_spacing("système linéaireAx =b, SoitA∈ M"), "système linéaire Ax =b, Soit A∈ M")
        for text in ["Le PDF et NASA", "iPhone 15", "GitHub et macOS", "LaTeX marche.", "un mot."]:
            self.assertEqual(fix_spacing(text), text)
