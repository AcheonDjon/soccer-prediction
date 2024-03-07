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
        'Home_xG' :  filtered_home_df['Home_xG'].mean()*.8,
        'Home_shots' :  filtered_home_df['Home_shots'].mean()*0.8,
        'Home_corner' :  filtered_home_df['Home_corner'].mean() * 0.8,
        'Home_PK_Goal' :  filtered_home_df['Home_PK_Goal'].mean() * 0.8,
        'Home_PK_shots' :  filtered_home_df['Home_PK_shots'].mean()   ,
        'Home_ToP' :  filtered_home_df['Home_ToP'].mean() ,
        'Home_Elo': elo_dict[team_name]
      },index=[0]   
    )
    
   return average_home

def average_stats_second_team(team_name):
    filtered_away_df = df[df["HomeTeam"] == team_name]
    average_away = pd.DataFrame(
        {
          'Away_xG' :  filtered_away_df['Home_xG'].mean() * 0.8, 
          'Away_shots' :  filtered_away_df['Home_shots'].mean() * 0.8,
          'Away_corner' :  filtered_away_df['Home_corner'].mean() * 0.8,
          'Away_PK_Goal' :  filtered_away_df['Home_PK_Goal'].mean() * 0.8,
          'Away_PK_shots' :  filtered_away_df['Home_PK_shots'].mean() * 0.8,
          'Away_ToP' :  filtered_away_df['Home_ToP'].mean() * 0.8,
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

    # # # combining the two arrays together 
    df_combined = pd.concat([first_team_stats, second_team_stats], axis=1)

    print(df_combined)  

    #ordering the columns in the way the model requires 
    # # df_combined = df_combined[['Home_xG', 'Away_xG', 'Home_shots', 'Away_shots', 'Home_corner', 'Away_corner', 'Home_PK_Goal', 'Away_PK_Goal', 'Home_PK_shots', 'Away_PK_shots', 'Home_ToP','home_elo_start', 'away_elo_start']]
    df_combined = df_combined[['Home_xG', 'Away_xG', 'Home_shots', 'Away_shots', 'Home_corner', 'Away_corner', 'Home_PK_Goal', 'Away_PK_Goal', 'Home_PK_shots', 'Away_PK_shots', 'Home_ToP','Away_ToP']]

    # Make predictions with the loaded model
    # prediction = loaded_model.predict(df_combined)

    pred_probab = loaded_model.predict_proba(df_combined)
    #class probability comes in for [0 and 1] - the classes are listed in sorted order so first is for away and then for home

    first_pred = pred_probab[0][1] #0 is the away team and 1 is the home team
    away_pred = pred_probab[0][0] #0 is the away team and 1 is the home team

    winner = first_team if first_pred>away_pred else second_team
    winner_type = "first" if first_pred>away_pred else "second"
    winner_probaba = first_pred if first_pred>away_pred else away_pred

    print(f"{first_team} vs {second_team} and the winner is {winner} -- ({winner_type}) -- with a prob of {pred_probab}. winner is {winner} with a probability of {winner_probaba}")
    
    print(f"The first team win probability is {first_pred} and the second team win probability is {away_pred}")
    print(f"------------------------------------")


    print(f"------------------------------------")


#print(f"The prediction is ... {HomeTeamWonOrNot}!")
