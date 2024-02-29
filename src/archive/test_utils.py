import unittest
from src.jr.utils import calculate_elo_rating

class TestCalculateEloRating(unittest.TestCase):
    def test_home_team_wins(self):
        home_team_elo = 1500
        away_team_elo = 1400
        outcome = 1
        expected_home_elo = 1508.8
        expected_away_elo = 1391.2

        new_home_elo, new_away_elo = calculate_elo_rating({}, home_team_elo, away_team_elo, outcome)

        self.assertAlmostEqual(new_home_elo, expected_home_elo, places=1)
        self.assertAlmostEqual(new_away_elo, expected_away_elo, places=1)

    def test_away_team_wins(self):
        home_team_elo = 1500
        away_team_elo = 1600
        outcome = 0
        expected_home_elo = 1483.2
        expected_away_elo = 1616.8

        new_home_elo, new_away_elo = calculate_elo_rating({}, home_team_elo, away_team_elo, outcome)

        self.assertAlmostEqual(new_home_elo, expected_home_elo, places=1)
        self.assertAlmostEqual(new_away_elo, expected_away_elo, places=1)

    def test_draw(self):
        home_team_elo = 1500
        away_team_elo = 1500
        outcome = 1
        expected_home_elo = 1504.0
        expected_away_elo = 1496.0

        new_home_elo, new_away_elo = calculate_elo_rating({}, home_team_elo, away_team_elo, outcome)

        self.assertAlmostEqual(new_home_elo, expected_home_elo, places=1)
        self.assertAlmostEqual(new_away_elo, expected_away_elo, places=1)

if __name__ == '__main__':
    unittest.main()