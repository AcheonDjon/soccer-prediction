import pickle
import pandas as pd
import numpy as np
import xgboost as xg

df = pd.read_csv('./data/regular_season_data.csv')

filtered_home_df = df[df["HomeTeam"] == 'FAR']
filtered_away_df = df[df["AwayTeam"] == 'SPR']

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
with open("xgboost_model.pkl", "rb") as f:
    loaded_model = pickle.load(f)

# Make predictions with the loaded model
predictions = loaded_model.predict_proba(df_combined)


print(f"The prediction is {predictions}")



