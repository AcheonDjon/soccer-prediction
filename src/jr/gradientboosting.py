from sklearn.ensemble import GradientBoostingClassifier
import pickle
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV

param_grid = {
    'max_depth': [3, 5, 7],
    'learning_rate': [0.1, 0.01, 0.001],
    'n_estimators': [100, 200, 300]
}

df = pd.read_csv('./data/NSL_regular_season_final_model_input.csv')

# Define the outcome function
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

X = df.iloc[:, 5:-4]
Y = df.apply(outcome, axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

classifier = GradientBoostingClassifier()
grid_search = GridSearchCV(classifier, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

best_params = grid_search.best_params_
best_model = grid_search.best_estimator_

y_pred = best_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(accuracy)

# Save the trained model to a file
with open("gradientboosting_model.pkl", "wb") as f:
    pickle.dump(best_model, f)