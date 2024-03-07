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

def load_csv_dataset(file_path):
    dataset=pd.read_csv(file_path, delimiter= ",",header=0)
    return dataset



#main starts here

def determine_team_outcome(row):
    if row['HomeScore'] > row['AwayScore']:
        return 1
    elif row['HomeScore'] == row['AwayScore']:
        if row['Home_xG'] >= row['Away_xG']:
            return 1
        else:
            return 0
    else:
        return 0

file_path = './data/elo_ratings.csv'

dataset = load_csv_dataset(file_path)

#axis = 0 means apply function to each column
#axis = 1 means apply function to each row
dataset['new_team1_rating'], dataset['new_team2_rating'] = zip(*dataset.apply(lambda row: compute_elo_rating(row['home_elo_start'], row['away_elo_start'], determine_team_outcome(row)), axis=1))

print(dataset.head())

# Save the updated dataset to a new CSV file
dataset.to_csv('./data/elo_ratings_updated.csv', index=False)



    