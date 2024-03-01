import time
from sklearn.datasets import load_iris
from sklearn.discriminant_analysis import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import xgboost


def load_csv_dataset(file_path):
    """
    Load a CSV data set from a file using pandas
    :param file_path: The path to the CSV file
    :return: A pandas DataFrame representing the data set
    """
    dataset = pd.read_csv(file_path, delimiter= ",",header=0)
    return dataset


def determine_outcome(row):
    """
    Determine the outcome of a soccer match based on the scores and expected goals
    :param row: A row from the dataset containing the scores and expected goals
    :return: 0 for home win, 1 for away win, 
    """
    if row['HomeScore'] > row['AwayScore']:
        return 0  # home win
    elif row['HomeScore'] == row['AwayScore']:
        if row['Home_xG'] >= row['Away_xG']: #TODO: check if this is correct whether to use xG or not
            return 0  # home win
        else:
            return 1  # away win
    else:
        return 1


start_time = time.time()

# Load the dataset
file_path = './data/elo_ratings.csv'
dataset = load_csv_dataset(file_path)
dataset['Outcome'] = dataset.apply(determine_outcome, axis=1)

# Setup y and X
y = dataset['Outcome']
X = dataset.drop(['Outcome', 'game_ordered_id'], axis=1)
col = X.columns
X = X.iloc[:, 5:]

# Normalize the data using StandardScaler
# X = StandardScaler().fit_transform(X)

# Split the dataset for training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=47)

# Train the xgboost model
# Hyperparameter tuning
from sklearn.model_selection import GridSearchCV

# Define the parameter grid for hyperparameter tuning
param_grid = {
    'learning_rate': [0.1, 0.01, 0.001],
    'max_depth': [3, 5, 7],
    'n_estimators': [100, 200, 300],
    'subsample': [0.6, 0.8, 1.0],
    'colsample_bytree': [0.6, 0.8, 1.0]
}

# Create an instance of the XGBoost classifier
xgb_model = xgboost.XGBClassifier()

# Perform grid search to find the best hyperparameters
grid_search = GridSearchCV(estimator=xgb_model, param_grid=param_grid, cv=5)
grid_search.fit(X_train, y_train)

# Get the best hyperparameters
best_params = grid_search.best_params_

# Make predictions on the test set
y_pred = grid_search.predict(X_test)

# Calculate accuracy score
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

end_time = time.time()
execution_time = end_time - start_time

print(f"Execution time: {execution_time} seconds")

# Get feature importance
feature_importance = grid_search.best_estimator_.feature_importances_

# Create a DataFrame to store feature importance
feature_importance_df = pd.DataFrame({'Importance': feature_importance})

# Sort the DataFrame by importance in descending order
feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

# Print the feature importance
print(feature_importance_df)
# Save the model
import pickle

# Save grid search results using pickle
with open('grid_search_results.pkl', 'wb') as f:
    pickle.dump(grid_search, f)