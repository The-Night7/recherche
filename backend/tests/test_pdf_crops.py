import unittest

from pdf_crops import locate, with_crops


def word(text, x, y, w=8.0, h=9.0):
    return (text, x, y, x + w, y + h)


# H = ∪n∈Z B∞(a = (1/2, n/2), 1/2) : pdftotext lit les numérateurs, puis la ligne, puis les dénominateurs
PAGE = (
    [word("Ainsi,", 100, 200, 30), word("on", 135, 200), word("peut", 146, 200, 20), word("montrer", 170, 200, 35)]
    + [word("1", 300, 239), word("n", 313, 239), word("1", 331, 239)]
    + [word("H", 200, 247), word("=", 213, 247), word("∪", 225, 247), word("n∈Z", 233, 250, 18),
       word("B", 256, 247), word("∞", 265, 250), word("a", 278, 247), word("=", 288, 247), word("(", 298, 247),
       word(",", 310, 247), word("),", 324, 247)]
    + [word("2", 300, 254), word("2", 313, 254), word("2", 331, 254)]
    + [word("Or", 100, 280, 12), word("une", 116, 280, 16), word("union", 136, 280, 24), word("infinie", 164, 280, 30)]
)
SOURCE = "H = ∪n∈Z\nB∞\na = (1\n2,\nn²\n),\n1\n2"


class PdfCropTests(unittest.TestCase):
    def test_stacked_formula_is_found_whatever_the_reading_order(self):
        found = locate(PAGE, SOURCE)
        self.assertIsNotNone(found)
        _, (x0, y0, x1, y1) = found
        self.assertLessEqual(x0, 200)
        self.assertGreaterEqual(x1, 339)
        self.assertLessEqual(y0, 239)          # numérateurs inclus
        self.assertGreaterEqual(y1, 263)       # dénominateurs inclus
        self.assertGreater(y0, 209)            # pas la phrase au-dessus
        self.assertLess(y1, 280)               # ni celle au-dessous

    def test_prose_is_not_shown_as_a_formula(self):
        self.assertIsNone(locate(PAGE, "X =Y p.s.)."))
        self.assertIsNone(locate(PAGE, "Or une union infinie d’ouverts est un ouvert donc H est un ouvert"))

    def test_only_located_blocks_get_a_crop(self):
        import pdf_crops
        original = pdf_crops.page_words
        pdf_crops.page_words = lambda path, number: PAGE
        try:
            md = with_crops("Texte\n\n   ```pdf\n   " + SOURCE.replace("\n", "\n   ") + "\n   ```\n\n```pdf\nX =Y p.s.).\n```",
                            "doc", "doc.pdf", [3])
        finally:
            pdf_crops.page_words = original
        self.assertIn("   ```pdf crop=doc=doc&n=3&box=", md)
        self.assertIn("\n```pdf\nX =Y", md)


if __name__ == "__main__":
    unittest.main()
