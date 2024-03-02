import pickle
import pandas as pd
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import xgboost as xg 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score 

df = pd.read_csv('./data/NSL_regular_season_final_model_input.csv')

#1 means the home team won
#0 means the away team won 
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


# df["Away_ToP"]= 1- df['Home_ToP']
X = df.iloc [:,5:-4]

print(X)

Y = df.apply(outcome, axis=1)


X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

#classifier = xg.XGBClassifier()
# classifer = RandomForestClassifier()
classifier = LogisticRegression(max_iter=10000) #0.75
#classifer = lgb.LGBMClassifier()
#classifer  = svm.SVC(kernel='linear')

classifier.fit(X_train, y_train)

#print feature importance
# Get feature importances
#importances = classifier.feature_importances_

# # Print feature importances
#for i, importance in enumerate(importances):
    #print(f"Feature {i}: {importance}")

y_pred = classifier.predict(X_test)

print(y_pred)
accuracy = accuracy_score(y_test, y_pred)

print(accuracy)
# df = df.drop(['game_id',"HomeTeam","AwayTeam","HomeScore",'AwayScore'], axis=1)


#save the model
# Save the trained model to a file
with open("xgboost_model.pkl", "wb") as f:
    pickle.dump(classifier, f)
