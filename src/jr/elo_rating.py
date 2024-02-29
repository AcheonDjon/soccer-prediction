import pandas as pd
regularteamsdata = pd.read_csv('./data/regular_season_data.csv')

home_rating1 = 1700
away_rating2 = 1500

def outcome(row):
    if row['HomeScore'] > row['AwayScore']:
        return 1
    elif row['HomeScore'] == row['AwayScore']:
        if row['Home_xG'] > row['Away_xG']:
            return 1
        else:
            return 0 
        
    else:
        return 0

def ELORATING(team1_rating, team2_rating, team1_result, k_factor=32):
    
      expected_result_team1 = 1 / (1 + 10 ** ((team2_rating - team1_rating) / 400))

    # Calculate the new Elo rating for team 1
      new_rating_team1 = team1_rating + k_factor * (team1_result - expected_result_team1)

    # Since the sum of the team's ratings should remain constant, the change in team 1's rating should be
    # subtracted from team 2's rating.
      new_rating_team2 = team2_rating + k_factor * ((1 - team1_result) - (1 - expected_result_team1))

      return new_rating_team1, new_rating_team2

print(ELORATING(home_rating1, away_rating2, 0))