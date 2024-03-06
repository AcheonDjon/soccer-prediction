import math
import pickle
import pandas as pd
import numpy as np
import xgboost as xg

df = pd.read_csv('./data/NSL_regular_season_data.csv')

gdf =pd.read_csv('./data/NSL_Knockout_Round_Games.csv')

#load elo rating from files
elo_dict = pd.read_csv('./data/NSL_regular_season_final_elo_ratings.csv')

#loaded the model 
# Load the saved model from file
loaded_model = None
with open("voted_best.pkl", "rb") as j:
    loaded_model = pickle.load(j)

def find_team(row):
  HomeTeam = row['TeamA']
  AwayTeam = row['TeamB']
  
  
def average_stats_first_team(team_name):
   filtered_home_df = df[df["HomeTeam"] == team_name]
   average_home = pd.DataFrame(
      {
        'Home_xG' :  filtered_home_df['Home_xG'].mean(),
        'Home_shots' :  filtered_home_df['Home_shots'].mean(),
        'Home_corner' :  filtered_home_df['Home_corner'].mean(),
        'Home_PK_Goal' :  filtered_home_df['Home_PK_Goal'].mean(),
        'Home_PK_shots' :  filtered_home_df['Home_PK_shots'].mean(),
        'Home_ToP' :  filtered_home_df['Home_ToP'].mean(),
        'Home_Elo': elo_dict[team_name]
      },index=[0]   
    )
    
   return average_home

def average_stats_second_team(team_name):
    filtered_away_df = df[df["HomeTeam"] == team_name]
    average_away = pd.DataFrame(
        {
          'Away_xG' :  filtered_away_df['Home_xG'].mean(),
          'Away_shots' :  filtered_away_df['Home_shots'].mean(),
          'Away_corner' :  filtered_away_df['Home_corner'].mean(),
          'Away_PK_Goal' :  filtered_away_df['Home_PK_Goal'].mean(),
          'Away_PK_shots' :  filtered_away_df['Home_PK_shots'].mean(),
          'Away_ToP' :  filtered_away_df['Home_ToP'].mean(),
          'Away_Elo': elo_dict[team_name]
        },index=[0]   
      )
    return average_away
   
   
for index, rowdata in gdf.iterrows():
    
    first_team  = rowdata['TeamA']
    #print(first_team)
    second_team = rowdata['TeamB']

    first_team_stats = average_stats_first_team(first_team) 
    # print(first_team_stats)

    second_team_stats = average_stats_second_team(second_team)
    # print(second_team_stats)
    
    first_elo = first_team_stats['Home_Elo'][0].astype(int)
    second_elo = second_team_stats['Away_Elo'][0].astype(int)

    print(f"{first_team} vs {second_team} and their elo scores are {first_elo} vs {second_elo}")

    # compute winning probability based on elo rating
    elo_diff = first_elo - second_elo
    win_prob = 1 / (1 + math.pow(10, -elo_diff/400))
    
    first_pred = win_prob
    second_pred = 1 - win_prob
    print(f"The winning probability for {first_team} is {win_prob:.2f} and for {second_team} is {1-win_prob:.2f}")


    winner = first_team if first_pred>second_pred else second_team
    winner_type = "first" if first_pred>second_pred else "second"
    winner_probaba = first_pred if first_pred>second_pred else second_pred

    print(f"{first_team} vs {second_team} and the winner is {winner} -- ({winner_type}) -- with a prob of {winner_probaba}. winner is {winner} with a probability of {winner_probaba}")
    
    print(f"The first team win probability is {first_pred} and the second team win probability is {second_pred}")
    print(f"------------------------------------")


    print(f"------------------------------------")


#print(f"The prediction is ... {HomeTeamWonOrNot}!")
