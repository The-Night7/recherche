import unittest
from pathlib import Path

import ingest
import ingest_series
from clean_extraction import clean_text
from reflow import big_sums, display_math, to_md_blocks


class ReadabilityTests(unittest.TestCase):
    def markdown(self, text):
        return to_md_blocks(text)[0]['text']

    def test_repeated_formula_parts_survive_import(self):
        pages = ['Université Exemple\nk=1\nn + 1\nun =\n1 −\n' + str(i)
                 for i in range(1, 6)]
        for importer in (ingest, ingest_series):
            with self.subTest(importer=importer.__name__):
                cleaned = importer.drop_running_lines(pages[:])
                self.assertNotIn('Université Exemple', '\n'.join(cleaned))
                for page in cleaned:
                    self.assertIn('k=1\nn + 1\nun =\n1 −', page)
                self.assertFalse(cleaned[2].endswith('\n3'))

    def test_arithmetic_signs_are_not_exponents(self):
        self.assertEqual(clean_text('k\n+\n1\nn\n−\n2'), 'k\n+\n1\nn\n−\n2')
        self.assertEqual(clean_text('R\nn'), 'Rⁿ')

    def test_fraction_at_end_is_complete(self):
        self.assertIn(r'\dfrac{1}{4}', self.markdown('un =\n1\n4'))

    def test_prose_is_not_an_exponential(self):
        text = self.markdown('On décompose cette fraction en élément simple\n1\nn')
        self.assertIn('élément simple', text)
        self.assertNotIn(r'e^{1/n}', text)
        self.assertIn(r'\dfrac{1}{n}', text)

    def test_shifted_and_infinite_sums(self):
        lines = big_sums(['nX+1', 'k=2', '1', 'k', '=', 'X', '+∞', 'k=1', 'uk'])
        math = display_math(lines)
        self.assertIn(r'\sum_{k=2}^{n+1} \dfrac{1}{k}', math)
        self.assertIn(r'\sum_{k=1}^{+\infty }', math)
        self.assertNotIn('k&=', math)

    def test_equations_are_separate_from_explanations(self):
        text = self.markdown('Réponse 4\n1. un =\n1\nn\nOn calcule la somme.\nun =\n1\nn + 1\n2. La série converge.')
        self.assertIn('#### Réponse 4', text)
        self.assertIn('   On calcule la somme.', text)
        self.assertIn('   $$\n', text)
        self.assertIn('\n2.\n', text)
        self.assertNotIn('On calcule', text.split('$$')[1])

    def test_short_math_in_a_sentence_stays_inline(self):
        text = self.markdown('Une fonction dans\nℝⁿ\n, avec n fixé.')
        self.assertNotIn('$$', text)
        self.assertIn('avec n fixé.', text)

    def test_opening_equivalence_and_its_explanation_stay_together(self):
        text = self.markdown('1. un ∼\n1\nn2\nqui est une suite de Riemann.')
        self.assertIn(r'$u_n\sim  \dfrac{1}{n^{2}}$ qui est', text)

    def test_logarithms_are_not_sequences(self):
        self.assertIn(r'\ln', display_math(['ln(k)']))
        self.assertNotIn('l_n', display_math(['ln(k)']))

    def test_embedded_summation_indices_do_not_break_alignment(self):
        math = display_math(['∀n ≥ 2, ∑_{k=2}^{n} 1', 'k', '=', '1'])
        self.assertNotIn('$', math)
        self.assertIn(r'\sum_{k=2}^{n}', math)

    def test_set_difference_and_literal_symbols_are_escaped(self):
        math = display_math([r'V \{a} #'])
        self.assertIn(r'\setminus \{a\}', math)
        self.assertIn(r'\#', math)

    def test_captured_exercise_is_complete_and_readable(self):
        source = Path('data/series/TD1Correction_20242025_Series_P2S1_DMaths.txt')
        for importer in (ingest, ingest_series):
            with self.subTest(importer=importer.__name__):
                args = (str(source), 'series') if importer is ingest else (str(source),)
                chunks = importer.chunk_document(*args)
                exercises = [c for c in chunks if c['section'].startswith('Exercice 4')]
                self.assertEqual(len(exercises), 1)
                text = self.markdown(exercises[0]['text'])
                self.assertIn('#### Réponse 4', text)
                self.assertIn(r'\sum_{k=1}^{n}', text)
                self.assertIn(r'\dfrac{1}{n + 1}', text)
                self.assertIn('\n4.\n', text.split('#### Réponse 4')[1])
                self.assertNotIn('nX+1', text)
                self.assertNotIn(r'\sum_{k&=', text)
                self.assertNotIn('élément simpl$', text)
                self.assertIn(r"\sum_{k'=2}^{n+1}", text)
                self.assertNotIn(r'k^{0}', text)


if __name__ == '__main__':
    unittest.main()
