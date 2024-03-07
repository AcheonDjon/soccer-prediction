
def game_outcome(row):
    """
    Determines the outcome of a soccer game based on the given row of data.

    Parameters:
    - row: A dictionary-like object representing the data of a soccer game.

    Returns:
    - 1 if the home team wins or the game is a draw and the home team had more expected goals,
    - 0 otherwise.
    """
    if row["HomeScore"] > row["AwayScore"]:
        return 1
    elif row["HomeScore"] == row["AwayScore"]:
        if row["Home_xG"] >= row["Away_xG"]:
            return 1
        else:
            return 0
    else:
        return 0
    

def calculate_elo_rating(row, home_team_elo, away_team_elo, outcome):
    """
    Calculates the new Elo ratings for two soccer teams based on the outcome of a game.

    Parameters:
    - home_team_elo: The current Elo rating of the home team.
    - away_team_elo: The current Elo rating of the away team.
    - outcome: 1 if the home team wins or the game is a draw and the home team had more expected goals,
               0 otherwise.

    Returns:
    - A tuple containing the new Elo ratings for the home team and the away team.
    """
    K = 32
    
    E_home = 1 / (1 + 10 ** ((away_team_elo - home_team_elo) / 400))
    E_away = 1 - E_home

    new_home_team_elo = home_team_elo + K * (outcome - E_home)
    new_away_team_elo = away_team_elo + K * ((1 - outcome) - E_away)

    return new_home_team_elo, new_away_team_elo 

import numpy as np

def win_probability_with_home_boost(elo_a, elo_b, home_field_boost):
    """
    Calculate the probability of Team A winning a match based on Elo ratings of both teams
    and a home field advantage boost.

    Parameters:
        elo_a (float): Elo rating of Team A.
        elo_b (float): Elo rating of Team B.
        home_field_boost (float): Boost factor for the home team.

    Returns:
        float: Probability of Team A winning.
    """
    # Calculate the difference in Elo ratings
    elo_diff = elo_b - elo_a

    # Adjust Elo difference with home field boost for the home team
    if home_field_boost > 0:
        elo_diff -= home_field_boost

    # Calculate win probability using the logistic function
    return 1 / (1 + 10 ** (elo_diff / 400))

# Example Elo ratings
elo_team_a = 1500
elo_team_b = 1500

# Example home field advantage boost
home_field_boost = 50  # Adjust as needed

# Calculate win probability with home field boost
probability_team_a_wins = win_probability_with_home_boost(elo_team_a, elo_team_b, home_field_boost)

print("Probability of Team A winning with home field boost:", probability_team_a_wins)
print("Probability of Team B winning with home field boost:", 1 - probability_team_a_wins)
print("Probability of a draw with home field boost:", 1 - probability_team_a_wins - (1 - probability_team_a_wins))