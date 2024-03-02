import pickle
import pandas as pd
import numpy as np
import xgboost as xg

df = pd.read_csv('./data/NSL_regular_season_data.csv')
gdf =pd.read_csv('./data/NSL_Group_Round_Games.csv')

#load elo rating from files
elo_dict = pd.read_csv('./data/NSL_regular_season_final_elo_ratings.csv')

#loaded the model 
# Load the saved model from file
loaded_model = None
with open("xgboost_model.pkl", "rb") as j:
    loaded_model = pickle.load(j)


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
        'Home_ToP' :  filtered_home_df['Home_ToP'].mean(),
        # 'home_elo_start': elo_dict[HomeTeam]
      },index=[0]
  )

  average_away = pd.DataFrame(
      {
        'Away_xG' :  filtered_away_df['Away_xG'].mean(),
        'Away_shots' :  filtered_away_df['Away_shots'].mean(),
        'Away_corner' :  filtered_away_df['Away_corner'].mean(),
        'Away_PK_Goal' :  filtered_away_df['Away_PK_Goal'].mean(),
        'Away_PK_shots' :  filtered_away_df['Away_PK_shots'].mean(),
        # 'away_elo_start': elo_dict[AwayTeam]
      },index=[0]
  )

  # print(average_home)
  # print(average_away)

  # combining the two arrays together 
  df_combined = pd.concat([average_away, average_home], axis=1)

  #ordering the columns in the way the model requires 
  # df_combined = df_combined[['Home_xG', 'Away_xG', 'Home_shots', 'Away_shots', 'Home_corner', 'Away_corner', 'Home_PK_Goal', 'Away_PK_Goal', 'Home_PK_shots', 'Away_PK_shots', 'Home_ToP','home_elo_start', 'away_elo_start']]
  df_combined = df_combined[['Home_xG', 'Away_xG', 'Home_shots', 'Away_shots', 'Home_corner', 'Away_corner', 'Home_PK_Goal', 'Away_PK_Goal', 'Home_PK_shots', 'Away_PK_shots', 'Home_ToP']]


  # Make predictions with the loaded model
  #predictions = loaded_model.predict_proba(df_combined)
  prediction = loaded_model.predict(df_combined)

  winner = HomeTeam if prediction == 1 else AwayTeam


  print(f"{HomeTeam} vs {AwayTeam} and the winner is {winner}")
  

HomeTeamWonOrNot=gdf.apply(find_team, axis=1)

#print(f"The prediction is ... {HomeTeamWonOrNot}!")
