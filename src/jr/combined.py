from customprobability import CustomVotingClassifier
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score 
from sklearn.model_selection import RandomizedSearchCV
df = pd.read_csv('./data/NSL_regular_season_final_model_input.csv')
# Load the pickled models
with open('logistic_regression.pkl', 'rb') as f:
    model1 = pickle.load(f)


with open('xgboost_model.pkl', 'rb') as f:
    model2 = pickle.load(f)

with open('gradientboosting_model.pkl', 'rb') as f:
    model3 = pickle.load(f)



# Create the VotingClassifier
voting_clf = CustomVotingClassifier(estimators=[
    ('model1', model1),
    ('model2', model2),
    ('model3', model3)]
)


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

# Fit the VotingClassifier
voting_clf.fit(X_train, y_train)

# Make predictions
predictions = voting_clf.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(accuracy)

with open("voting_class.pkl", "wb") as f:
  pickle.dump(voting_clf, f)
