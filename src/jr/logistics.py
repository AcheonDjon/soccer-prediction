import pickle
import pandas as pd
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import xgboost as xg 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score 
from sklearn.model_selection import GridSearchCV

param_grid = {
    'C': [0.001, 0.01, 0.1, 1, 10, 100],
    'penalty': ['l1', 'l2'],
    'solver': ['liblinear']
}

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
X['Away_ToP'] = 1- X['Home_ToP']
print(X)

Y = df.apply(outcome, axis=1)


X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

#classifier = xg.XGBClassifier()
# classifer = RandomForestClassifier()
classifier = LogisticRegression(max_iter=10000) #0.75
#classifer = lgb.LGBMClassifier()
#classifer  = svm.SVC(kernel='linear')
grid_search = GridSearchCV(classifier, param_grid, cv=5, scoring = 'accuracy')
grid_search.fit(X_train, y_train)

best_params = grid_search.best_params_
best_model = grid_search.best_estimator_




y_pred = best_model.predict(X_test)

print(y_pred)
accuracy = accuracy_score(y_test, y_pred)

print(accuracy)
# df = df.drop(['game_id',"HomeTeam","AwayTeam","HomeScore",'AwayScore'], axis=1)

# Print feature importance
feature_importance = best_model.coef_[0]
for feature, importance in zip(X.columns, feature_importance):
    print(f"{feature}: {importance}")

# Normalize feature importance
feature_importance /= len(feature_importance)

# Print feature importance
print("Normalized Feature Importance:", feature_importance)

#save the model
# Save the trained model to a file
with open("logistic_regression.pkl", "wb") as f:
    pickle.dump(best_model, f)
