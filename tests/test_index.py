import json
import tempfile
import unittest
from pathlib import Path
from collections import Counter

import numpy as np

from build_index import main
from search import load_index, query_vector, search
from text_utils import tokenize


class SparseIndexTests(unittest.TestCase):
    def test_sparse_build_and_search_match_dense_tfidf_including_empty_passages(self):
        chunks = [dict(course='analyse1', year=2024, kind='cours', corrige=False,
                       section='', label=str(i), text=text)
                  for i, text in enumerate(('matrice matrice diagonale', '', 'produit scalaire matrice', 'scalaire'))]
        with tempfile.TemporaryDirectory() as folder:
            source, index, vocabulary = [str(Path(folder) / name) for name in ('chunks.json', 'index.npz', 'vocab.json')]
            Path(source).write_text(json.dumps(chunks))
            main(source, index, vocabulary)
            matrix, idf, vocab, loaded = load_index(index, vocabulary, source)
            tf = np.zeros(matrix.shape)
            for row, chunk in enumerate(chunks):
                for word, count in Counter(tokenize(chunk['text'])).items():
                    tf[row, vocab[word]] = count
            expected_idf = np.log((1 + len(chunks)) / (1 + (tf > 0).sum(axis=0))) + 1
            dense = tf * expected_idf
            norms = np.linalg.norm(dense, axis=1)
            dense /= np.where(norms > 0, norms, 1)[:, None]
            vector, _ = query_vector('matrice scalaire', vocab, idf)
            np.testing.assert_allclose(idf, expected_idf, rtol=1e-6)
            np.testing.assert_allclose(matrix @ vector, dense @ vector, rtol=1e-6)
            sparse_results, _ = search('matrice scalaire', matrix, idf, vocab, loaded)
            dense_results, _ = search('matrice scalaire', dense, idf, vocab, loaded)
            self.assertEqual([c['label'] for c, _ in sparse_results], [c['label'] for c, _ in dense_results])
