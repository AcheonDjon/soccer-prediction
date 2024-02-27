import pandas as pd
import xgboost
from sklearn.model_selection import train_test_split 

df = pd.read_csv('./data/regular_season_data.csv')


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

df['Outcome'] = df.apply(outcome, axis=1)

print (df[['Outcome','HomeScore']])

# X = df[[outcome]]
# Y = df[[]]
# df = df.drop(['game_id',"HomeTeam","AwayTeam","HomeScore",'AwayScore'], axis=1)