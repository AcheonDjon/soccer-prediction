
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

    row['Home_Elo_Start'] =  new_home_team_elo
    row['Away_Elo_Start'] =  new_away_team_elo

    return new_home_team_elo, new_away_team_elo

        