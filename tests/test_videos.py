import unittest
from urllib.parse import parse_qs, urlparse

import videos


def notions(chunk):
    return [v["notion"] for v in videos.annotate([chunk])[0]["_videos"]]


def query(chunk):
    url = videos.annotate([chunk])[0]["_videos"][0]["url"]
    return parse_qs(urlparse(url).query)["search_query"][0]


class VideoTests(unittest.TestCase):
    def test_exercise_is_linked_to_its_notions(self):
        chunk = {"course": "algebre-lineaire", "kind": "td", "section": "Exercice 3",
                 "text": "Exercice 3. La matrice A est-elle diagonalisable ? Déterminer ses valeurs propres."}
        self.assertEqual(set(notions(chunk)), {"Diagonalisation", "Valeurs propres et vecteurs propres"})
        self.assertTrue(query(chunk).endswith(" exercice corrigé"))

    def test_course_passage_searches_for_a_lesson(self):
        chunk = {"course": "series", "kind": "cours", "section": "Séries entières",
                 "text": "Le rayon de convergence d'une série entière…"}
        self.assertEqual(notions(chunk)[0], "Séries entières")
        self.assertEqual(query(chunk), "Séries entières cours")

    def test_whole_words_and_domains(self):
        # « rang$ » ne trouve pas « range » ; les graphes de fonctions ne sont pas des graphes (informatique)
        self.assertEqual(notions({"course": "algebre2", "kind": "td", "text": "on range le graphe de f"}), [])
        # SHS : pas de vidéo
        self.assertEqual(notions({"course": "shs", "kind": "cours", "text": "série entière"}), [])
        self.assertEqual(notions({"course": "ing-1-s1-gm-unix", "kind": "td", "text": "La commande grep"}),
                         ["Commandes Unix et shell"])

    def test_split_exercise_reuses_the_videos_of_its_start(self):
        chunks = videos.annotate([
            {"course": "analyse1", "kind": "td", "doc": "d", "section": "Exercice 2", "text": "Calculer le développement limité"},
            {"course": "analyse1", "kind": "td", "doc": "d", "section": "Exercice 2", "text": "à l'ordre 3 en 0."},
            {"course": "analyse1", "kind": "td", "doc": "d", "section": "Exercice 3", "text": "Montrer que 2 + 2 = 4."},
        ])
        self.assertEqual(chunks[1]["_videos"], chunks[0]["_videos"])
        self.assertEqual(chunks[2]["_videos"], [])


if __name__ == "__main__":
    unittest.main()
