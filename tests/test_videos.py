import unittest
from urllib.parse import parse_qs, urlparse

import videos


def notions(chunk):
    return [v["notion"] for v in videos.annotate([chunk])[0]["_videos"]]


def query(chunk):
    url = videos.annotate([chunk])[0]["_videos"][0]["url"]
    return parse_qs(urlparse(url).query)["search_query"][0]


class VideoTests(unittest.TestCase):
    def test_exercise_without_channel_video_searches_corrected_exercises(self):
        chunk = {"course": "analyse1", "kind": "td", "text": "Exercice 1. Donner le développement limité de sin."}
        self.assertTrue(query(chunk).endswith(" exercice corrigé"))

    def test_exercise_is_linked_to_its_notions(self):
        chunk = {"course": "algebre-lineaire", "kind": "td", "section": "Exercice 3",
                 "text": "Exercice 3. La matrice A est-elle diagonalisable ? Déterminer ses valeurs propres."}
        self.assertEqual(set(notions(chunk)), {"Diagonalisation", "Valeurs propres et vecteurs propres"})

    def test_notion_without_channel_video_searches_youtube(self):
        chunk = {"course": "analyse1", "kind": "cours", "section": "Développements limités",
                 "text": "Le développement limité à l'ordre 2 en 0…"}
        self.assertEqual(notions(chunk)[0], "Développements limités")
        self.assertEqual(query(chunk), "Développements limités cours")

    def test_channel_video_is_chosen_by_keywords(self):
        def first(text):
            return videos.annotate([{"course": "algebre1", "kind": "td", "text": text}])[0]["_videos"][0]
        video = first("Calculer le module du nombre complexe z.")
        self.assertEqual(video["url"], "https://www.youtube.com/watch?v=knME7MU3EmQ")
        self.assertEqual((video["title"], video["channel"]), ("Nombres complexes 4/12 : Module", "Maths Adultes"))
        # sans mot-clé particulier : la première vidéo de la notion
        self.assertEqual(first("Soit un nombre complexe.")["url"], "https://www.youtube.com/watch?v=Iphz0Np1-_k")

    def test_catalogue_videos_belong_to_known_notions_and_channels(self):
        names = {n[0] for n in videos.NOTIONS}
        for notion, vids in videos.VIDEOS.items():
            self.assertIn(notion, names)
            for channel, vid, title, _ in vids:
                self.assertIn(channel, videos.CHANNELS)
                self.assertRegex(vid, r"^[\w-]{11}$")
                self.assertTrue(title)

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
