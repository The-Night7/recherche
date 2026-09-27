import re
import tempfile
import unittest
from pathlib import Path

import ingest
import ingest_series
from clean_extraction import clean_text
from reflow import big_sums, display_math, is_math_line, math_only, restore_large_parentheses, to_md_blocks


class ReadabilityTests(unittest.TestCase):
    def markdown(self, text):
        return to_md_blocks(text)[0]['text']

    def test_answer_after_statement_starts_its_own_section(self):
        text = ('Exercice 2\n1. Déterminer la nature.\n2. Calculer la somme.\n'
                'Réponse. 1. On reconnait une série de Riemann.\n2. Le résultat vaut 9.')
        md = self.markdown(text)
        self.assertRegex(md, r'2\.\n\n   Calculer la somme\.\n\n#### Réponse\n\n1\.\n\n   On reconnait')
        self.assertNotIn('Réponse.', md)
        self.assertEqual(self.markdown('Réponse 4\nOui.'), '#### Réponse 4\n\nOui.')

    def test_math_typography_follows_the_sentence(self):
        text = ('Exercice 2\nPour n ≥ 2 on considère la série de terme général un =\n2n + 3\nn(n2 − 1).\n'
                'Réponse. 1. On en déduit que un ∼\n2n\nn3 =\n2\nn2\nqui converge. La série un converge.\n'
                '2. Le dénominateur se factorise : n(n\n2 − 1) = (n + 1)n(n − 1), d’où la décomposition de un en éléments simples.')
        md = self.markdown(text)
        self.assertIn(r'$u_n = \dfrac{2n + 3}{n(n^{2} - 1)}$.', md)
        self.assertIn(r'$u_n \sim \dfrac{2n}{n^{3}} = \dfrac{2}{n^{2}}$', md)
        self.assertIn('La série $u_n$ converge', md)
        self.assertIn('décomposition de $u_n$ en éléments', md)
        self.assertIn('n(n² − 1)', md)
        self.assertNotIn('.}', md)
        self.assertEqual(self.markdown('Il y a un enfant et un chat.'), 'Il y a un enfant et un chat.')

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

    def test_large_parentheses_recover_without_changing_factorials(self):
        source = ' \n(n + 1)!\n+\n1\nn + 2!'
        expected = '(\n(n + 1)!\n+\n1\nn + 2)'
        self.assertEqual(restore_large_parentheses(source), expected)
        self.assertEqual(restore_large_parentheses(expected), expected)
        for factorial in ('n!', '(n + 1)!', 'n + (n + 1)!'):
            self.assertEqual(restore_large_parentheses(factorial), factorial)
        self.assertEqual(restore_large_parentheses(' \nn + 1\nEx.6\n!'), ' \nn + 1\nEx.6\n!')

    def test_long_sum_from_capture_is_rendered_with_all_three_groups(self):
        chunks = ingest.chunk_document('data/series/TD1Correction_20242025_Series_P2S1_DMaths.txt', 'series')
        exercise = next(c for c in chunks if c['section'] == 'Exercice 4')
        text = self.markdown(exercise['text'])
        calculation = text.split('On va réunir les valeurs de k comprises entre k = 3 et k = n', 1)[1].split('Les trois dernières sommes', 1)[0]
        self.assertNotIn('```pdf', calculation)
        self.assertIn(r'\begin{aligned}', calculation)
        first_equality = calculation.split(r'\begin{aligned}', 1)[1].split('\n   &=', 1)[0]
        compact = lambda s: re.sub(r'\s+', '', s.replace('\\\\', '').replace('&', ''))
        expected = (
            r'\sum_{k=1}^{n} u_k = \dfrac{1}{2} (1 + \dfrac{1}{2} + \sum_{k=3}^{n} \dfrac{1}{k})'
            r' - (\dfrac{1}{2} + \sum_{k=3}^{n} \dfrac{1}{k} + \dfrac{1}{n + 1})'
            r' + \dfrac{1}{2} (\sum_{k=3}^{n} \dfrac{1}{k} + \dfrac{1}{n + 1} + \dfrac{1}{n + 2})'
        )
        self.assertEqual(compact(first_equality), compact(expected))
        self.assertIn('\n   &+', first_equality)
        self.assertIn('\n   &-', first_equality)

    def test_integral_bounds_and_differential_stay_together(self):
        text = self.markdown('∀k ≥ 2,\nZ k+1\nk\ndt\ntln t\n=\nZ n+1\n2\ndt =\n1')
        self.assertIn(r'\int_{k}^{k+1} \dfrac{dt}{t \ln  t}', text)
        self.assertIn(r'\int_{2}^{n+1} dt', text)
        self.assertNotIn(r'\dfrac{Z', text)
        self.assertNotIn('dt &=', text)
        self.assertIn('Z', display_math(['Z a', 'b', '=', 'c']))
        self.assertNotIn(r'\int', display_math(['Z a', 'b', '=', 'dt']))
        self.assertEqual(display_math(['dy', 'dx']), r'\dfrac{dy}{dx}')

    def test_compact_logarithms_are_functions_and_not_sequence_indices(self):
        for denominator in ('tln2t', 't ln2 t', 't ln2t'):
            text = self.markdown('1\n' + denominator)
            self.assertIn(r'\dfrac{1}{t \ln^{2} t}', text)
            self.assertNotIn('l_n', text)
        self.assertIn(r'\ln^{2} t', display_math(['ln2t']))
        self.assertFalse(math_only('On additionne les valeurs.'))

    def test_embedded_fractions_and_series_stay_in_their_sentence(self):
        text = self.markdown('1. La fonction f(t) = 1\nt ln t\nest décroissante.\n'
                             'La série ∑n≥2\n1\nn ln2n\nest convergente.')
        self.assertIn(r'La fonction $f(t) = \dfrac{1}{t \ln  t}$ est décroissante.', text)
        self.assertIn(r'La série $\sum_{n\ge 2} \dfrac{1}{n \ln^{2} n}$ est convergente.', text)
        self.assertNotIn('$$', text)
        partial = self.markdown('Soit ∑n∈N\n(z ↦ an zⁿ\n) une série entière.')
        self.assertNotIn('```', partial)
        self.assertIn(') une série entière.', partial)

    def test_evaluation_bounds_are_not_a_fraction(self):
        self.assertEqual(display_math(['[t]', 'k+1', 'k']), r'[t]_{k}^{k+1}')
        self.assertEqual(display_math(['[ln(ln t)]n+1', '2']), r'[\ln (\ln  t)]_{2}^{n+1}')
        self.assertEqual(display_math(['[', '1', 'ln t', ']n+1', '2']),
                         r'[\dfrac{1}{\ln  t}]_{2}^{n+1}')
        for importer in (ingest, ingest_series):
            self.assertEqual(clean_text(importer.fix_glyphs('\x14\n1\nln t\n\x15n+1\n2')),
                             '[\n1\nln t\n]n+1\n2')

    def test_bertrand_capture_has_complete_integrals_without_invented_derivatives(self):
        for importer in (ingest, ingest_series):
            path = 'data/series/TD1Correction_20242025_Series_P2S1_DMaths.txt'
            args = (path, 'series') if importer is ingest else (path,)
            exercise = next(c for c in importer.chunk_document(*args) if c['section'] == 'Exercice 5')
            text = self.markdown(exercise['text'])
            # Only the two calculations with damaged derivative glyphs have
            # a collapsed source; their integral and result remain visible.
            self.assertEqual(text.count('```pdf-steps'), 2)
            visible = re.sub(r'```pdf-steps.*?```', '', text, flags=re.S)
            self.assertNotIn('```pdf', visible)
            self.assertNotIn('tln', visible)
            self.assertNotIn('l_n', visible)
            self.assertNotIn('Z ', visible)
            self.assertNotIn('}{0}', visible)
            self.assertIn(r'\int_{2}^{n+1} \dfrac{dt}{t \ln  t}', visible)
            self.assertIn(r'\int_{2}^{n+1} \dfrac{dt}{t \ln^{2} t}', visible)
            self.assertIn(r'\dfrac{1}{\ln  2} - \dfrac{1}{\ln (n + 1)}', visible)
            self.assertIn(r'[t]_{k}^{k+1}', visible)
            answer = visible.split('#### Réponse 5')[1]
            self.assertEqual(re.findall(r'^\d+\.$', answer, re.M), ['1.', '2.', '3.', '4.'])
            self.assertEqual(answer.count('$$'), 16)  # Eight complete calculation blocks.

    def test_readable_integral_identity_keeps_every_step(self):
        text = self.markdown('Z 1\n0\ndt\n=\n[t]\n1\n0\n=\n1 − 0\n=\n1')
        self.assertNotIn('```', text)
        self.assertIn(r'\int_{0}^{1} dt', text)
        self.assertIn(r'[t]_{0}^{1}', text)
        self.assertIn('1 - 0', text)

    def test_isolated_damaged_integral_has_no_empty_math_panel(self):
        text = self.markdown('Z n+1\n2\n(ln t)\n0\nln2\nt\ndt')
        self.assertIn('```pdf', text)
        self.assertNotIn('$$', text)
        self.assertNotIn('}{0}', text)

    def test_latex_font_artifacts(self):
        # ‖·‖ extrait en k·k, r″ en r00 (parfois coupé à la ligne), ⇔ en ⇐⇒, page 22 collée en exposant.
        md = self.markdown('x0 ∈ Bk·k2(a, r00) ⇐⇒ kx0 − ak2 < r00\nAinsi le rayon est r\n00/α\n'
                           '(puisque R = r\n00/α, r00 = αR).\nDonc ∃R > 0 et x ∈ R ⊂ A²²')
        self.assertIn(r'\Leftrightarrow', md)
        self.assertIn(r"\| x0 - a\| _{2} < r''", md)
        self.assertIn('(puisque R = r″/α, r″ = αR).', md)
        self.assertIn('∃R > 0', md)
        self.assertIn('x ∈ ℝ', md)
        self.assertNotIn('```pdf', md)
        self.assertNotIn('²²', md)
        self.assertEqual(self.markdown('Il donne un coup de pied (kick) et 11h00 sur Zoom.'),
                         'Il donne un coup de pied (kick) et 11h00 sur Zoom.')

    def test_set_exercise_statement(self):
        md = self.markdown('Exercice 2 :\nDéterminer si les ensembles suivants sont ouverts.\n'
                           '4. E = N\n5. F = {(x, y) ∈ R\n2/ x2 + y2 < 4}\n6. f(x, y) 6= (0, 0)')
        self.assertIn(r'E = \mathbb{N}', md)
        self.assertIn(r'\mathbb{R} ^{2}/ x^{2} + y^{2} < 4', md)
        self.assertIn(r'\neq', md)
        self.assertNotIn('dfrac', md)
        self.assertIn('d(Z, Y)', self.markdown('On a d(X, Y) ≤ d(X, Z) + d(Z, Y) pour tout X.'))


if __name__ == '__main__':
    unittest.main()
