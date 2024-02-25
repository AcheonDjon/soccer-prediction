import pandas as pd 


def compute_elo_rating(team1_rating, team2_rating, team1_result):
    """
    Compute the Elo ratings of two teams based on the result of a match.

    Parameters:
    - team1_rating (int): The current Elo rating of team 1.
    - team2_rating (int): The current Elo rating of team 2.
    - team1_result (float): The result of the match for team 1 (0 for loss, 0.5 for draw, 1 for win).

    Returns:
    - new_team1_rating (int): The updated Elo rating of team 1.
    - new_team2_rating (int): The updated Elo rating of team 2.
    """

    # Constants
    K = 32  # Elo rating update constant

    # Calculate expected scores
    team1_expected = 1 / (1 + 10 ** ((team2_rating - team1_rating) / 400))
    team2_expected = 1 - team1_expected

    # Update ratings
    new_team1_rating = team1_rating + K * (team1_result - team1_expected)
    new_team2_rating = team2_rating + K * ((1 - team1_result) - team2_expected)

    return new_team1_rating, new_team2_rating

print(compute_elo_rating(1500, 1500, 1))

# def load_csv_dataset(file_path):
#     dataset=pd.read_csv(file_path, delimiter= ",",header=0)
#     return dataset
# file_path = './data/elo_ratings.csv'

# def elodata():
    