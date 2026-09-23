import re
import tempfile
import unittest
from pathlib import Path

import ingest
import ingest_series
from clean_extraction import clean_text
from reflow import big_sums, display_math, is_math_line, math_only, to_md_blocks


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
                rendered = re.sub(r"```pdf.*?```", "", text, flags=re.S)
                self.assertNotIn('nX+1', rendered)
                self.assertNotIn(r'\sum_{k&=', text)
                self.assertNotIn('élément simpl$', text)
                self.assertIn(r"\sum_{k'=2}^{n+1}", text)
                self.assertNotIn(r'k^{0}', text)

    def test_headings_and_question_markers_are_never_math(self):
        for marker in ('Ex.5', 'Ex. 6', 'Exercice 7', 'a)', 'b)', '(c)', '2.'):
            with self.subTest(marker=marker):
                self.assertFalse(math_only(marker))
                self.assertFalse(is_math_line(marker))

    def test_adjacent_exercise_cannot_change_previous_formula(self):
        first = self.markdown('Ex.5\na)\nf(x) =\n1\nx')
        combined = self.markdown('Ex.5\na)\nf(x) =\n1\nx\nEx.6\nCalculer les limites :')
        self.assertEqual(combined.split('#### Exercice 6')[0].strip(), first)
        self.assertIn(r'\dfrac{1}{x}', first)
        self.assertNotIn(r'\dfrac{1}{a}', first)

    def test_limit_and_expression_share_the_question_block(self):
        for limit in ('limx→0', 'lim x→0', 'lim\nx→0'):
            text = self.markdown('Ex.6\na)\n' + limit + '\nsin(x)\nx\nb)\ncosh(x)')
            formulas = re.findall(r'\$\$(.*?)\$\$', text, re.S)
            self.assertEqual(len(formulas), 2)
            self.assertIn(r'\lim', formulas[0])
            self.assertIn(r'\dfrac{\sin (x)}{x}', formulas[0])
            self.assertIn(r'\cosh', formulas[1])
            self.assertNotIn('a)', formulas[0])

    def test_ambiguous_fraction_is_preserved_in_one_source_block(self):
        source = 'limx→0\n4 sin3(x) + x − 4(cos(x) − 1)\n3x\n2 + ex − 1'
        text = self.markdown('a)\n' + source + '\nb)\ncosh(x)')
        block = re.search(r'```pdf\n(.*?)\n   ```', text, re.S).group(1)
        self.assertEqual(block.replace('   ', ''), source)
        self.assertNotIn(r'\dfrac{3x}', text)
        self.assertNotIn('b)', block)

    def test_both_captured_exercises_have_stable_structure(self):
        source = 'data/series/TD1_20192020_Series_P2S1_DMaths.txt'
        for importer in (ingest, ingest_series):
            args = (source, 'series') if importer is ingest else (source,)
            chunks = importer.chunk_document(*args)
            for number, letters in ((5, 'ab'), (6, 'abc')):
                selected = [c for c in chunks if c['section'] == f'Exercice {number}']
                self.assertEqual(len(selected), 1)
                text = self.markdown(selected[0]['text'])
                self.assertIn(f'#### Exercice {number}', text)
                for letter in letters:
                    self.assertIn('\n' + letter + ')\n', text)
                self.assertEqual(text.count('```pdf'), len(letters))
                self.assertNotIn(r'\dfrac', text)

    def test_short_exercises_are_neither_merged_nor_dropped(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / 'TD1_20242025_Series_P2S1_DMaths.txt'
            source.write_text('Ex.1\nCalculer : 1 + 1.\nEx.2\nCalculer : 1 + 1.\n', encoding='utf8')
            for importer in (ingest, ingest_series):
                args = (str(source), 'series') if importer is ingest else (str(source),)
                self.assertEqual([c['section'] for c in importer.chunk_document(*args)], ['Exercice 1', 'Exercice 2'])

    def test_parentheses_inside_prose_do_not_create_isolated_math_boxes(self):
        text = self.markdown('Une application définie sur\n(R²\n, avec une norme donnée).')
        self.assertNotIn('```pdf', text)
        self.assertNotIn('$$', text)
        self.assertIn('avec une norme donnée).', text)

    def test_closing_variable_is_not_a_question_marker(self):
        text = self.markdown('a)\nf(x) = (\nx)')
        self.assertEqual(re.findall(r'^[a-z]\)$', text, re.M), ['a)'])
        self.assertIn('f(x) = (x)', text)


if __name__ == '__main__':
    unittest.main()
