import pandas as pd
import xgboost as xg 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score 


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

X = df.iloc [:,5:]

Y = df.apply(outcome, axis=1)




X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

classifier = xg.XGBClassifier()

classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

print(y_pred)
accuracy = accuracy_score(y_test, y_pred)

print(accuracy)
# df = df.drop(['game_id',"HomeTeam","AwayTeam","HomeScore",'AwayScore'], axis=1)