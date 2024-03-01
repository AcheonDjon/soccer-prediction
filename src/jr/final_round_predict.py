import pickle
import pandas as pd
import numpy as np
import xgboost as xg

df = pd.read_csv('./data/NSL_regular_season_data_2 (1).csv')
gdf =pd.read_csv('./data/NSL_Group_Round_Games (6).csv')

def find_team(row):
  HomeTeam = row['HomeTeam']
  AwayTeam = row['AwayTeam']
  filtered_home_df = df[df["HomeTeam"] == HomeTeam]
  filtered_away_df = df[df["AwayTeam"] == AwayTeam]

  # print(filtered_home_df.count())

  # Structure of X test that goes into X test 
  #Home_xG  Away_xG  Home_shots  Away_shots  Home_corner  Away_corner  Home_PK_Goal  Away_PK_Goal  Home_PK_shots  Away_PK_shots  Home_ToP
  average_home = pd.DataFrame(
      {
        'Home_xG' :  filtered_home_df['Home_xG'].mean(),
        'Home_shots' :  filtered_home_df['Home_shots'].mean(),
        'Home_corner' :  filtered_home_df['Home_corner'].mean(),
        'Home_PK_Goal' :  filtered_home_df['Home_PK_Goal'].mean(),
        'Home_PK_shots' :  filtered_home_df['Home_PK_shots'].mean(),
        'Home_ToP' :  filtered_home_df['Home_ToP'].mean()

      },index=[0]
  )

  average_away = pd.DataFrame(
      {
        'Away_xG' :  filtered_away_df['Away_xG'].mean(),
        'Away_shots' :  filtered_away_df['Away_shots'].mean(),
        'Away_corner' :  filtered_away_df['Away_corner'].mean(),
        'Away_PK_Goal' :  filtered_away_df['Away_PK_Goal'].mean(),
        'Away_PK_shots' :  filtered_away_df['Away_PK_shots'].mean(),

      },index=[0]
  )

  # print(average_home)
  # print(average_away)
  df_combined = pd.concat([average_away, average_home], axis=1)

  df_combined = df_combined[['Home_xG', 'Away_xG', 'Home_shots', 'Away_shots', 'Home_corner', 'Away_corner', 'Home_PK_Goal', 'Away_PK_Goal', 'Home_PK_shots', 'Away_PK_shots', 'Home_ToP']]

  print(df_combined)


  # Load the saved model from file
  with open("xgboost_model.pkl", "rb") as j:
      loaded_model = pickle.load(j)

  # Make predictions with the loaded model
  predictions = loaded_model.predict_proba(df_combined)
  prediction = loaded_model.predict(df_combined)

  winner = HomeTeam if prediction == 1 else AwayTeam

  easyprint = f"the winner of the game is {winner}"

  tup_output = (predictions,HomeTeam,AwayTeam)
  
  return(tup_output)
# for i in gdf.iterrows():
#    HomeTeamGroup = gdf['HomeTeam']
#    AwayTeamGroup = gdf['AwayTeam']
#    HomeTeamWonOrNot=find_team(HomeTeamGroup, AwayTeamGroup)
  
# gdf.drop('game_id', axis=1)
HomeTeamWonOrNot=gdf.apply(find_team, axis=1)
print(f"The prediction is ... {HomeTeamWonOrNot}!")
