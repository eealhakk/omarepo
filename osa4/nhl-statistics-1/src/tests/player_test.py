import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    """Testausta varten luotu stub-luokka, joka palauttaa kiinteän pelaajalistan."""
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),    # 16 pistettä
            Player("Lemieux", "PIT", 45, 54),   # 99 pistettä
            Player("Kurri", "EDM", 37, 53),     # 90 pistettä
            Player("Yzerman", "DET", 42, 56),   # 98 pistettä
            Player("Gretzky", "EDM", 35, 89)    # 124 pistettä
        ]


class TestStatisticsService(unittest.TestCase):
    """Yksikkötestit StatisticsService-luokalle."""

    def setUp(self):
        """Luodaan StatisticsService-olio, jolle annetaan stub-luokka."""
        self.stats = StatisticsService(PlayerReaderStub())

    # --- search-metodin testit ---

    def test_search_returns_correct_player_when_found(self):
        """search palauttaa oikean pelaajan, jos nimi löytyy."""
        player = self.stats.search("Kurri")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Kurri")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.points, 90)

    def test_search_returns_none_when_player_not_found(self):
        """search palauttaa None, jos pelaajaa ei löydy."""
        player = self.stats.search("Selänne")
        self.assertIsNone(player)

    # --- team-metodin testit ---

    def test_team_returns_all_players_from_team(self):
        """team palauttaa kaikki saman joukkueen pelaajat."""
        edm_players = self.stats.team("EDM")
        names = [p.name for p in edm_players]
        self.assertEqual(len(edm_players), 3)
        self.assertCountEqual(names, ["Semenko", "Kurri", "Gretzky"])

    def test_team_returns_empty_list_for_unknown_team(self):
        """team palauttaa tyhjän listan, jos joukkuetta ei löydy."""
        players = self.stats.team("XYZ")
        self.assertEqual(players, [])

    # --- top-metodin testit ---

    def test_top_returns_requested_number_of_players_plus_one(self):
        """top palauttaa how_many + 1 pelaajaa, koska i <= how_many."""
        top_players = self.stats.top(2)
        self.assertEqual(len(top_players), 3)

    def test_top_players_are_sorted_by_points(self):
        """top palauttaa pelaajat pistejärjestyksessä laskevasti."""
        top_players = self.stats.top(4)
        points = [p.points for p in top_players]
        self.assertTrue(all(points[i] >= points[i + 1] for i in range(len(points) - 1)))
        self.assertEqual(top_players[0].name, "Gretzky")  # eniten pisteitä


if __name__ == "__main__":
    unittest.main()
