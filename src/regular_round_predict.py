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
    if row['HomeScore'] > row['AwayScore']:
        return 0 #home win
    #adding resolution for draws
    elif row['HomeScore'] == row['AwayScore']:
           if row['Home_xG'] >= row['Away_xG']:
              return 0 #home win        
           else:
              return 1 #away win
    else:
        return 1 

start_time = time.time() 

# Load the dataset
file_path = './data/elo_ratings.csv'
dataset = load_csv_dataset(file_path)
dataset['Outcome'] = dataset.apply(determine_outcome, axis=1)
# print(dataset)

#setup y and X
y = dataset['Outcome']  # Assuming 'Outcome' column contains the target variable
X = dataset.drop(['Outcome'], axis=1)  # Assuming 'Outcome' column contains the target variable
X = X.iloc[:, 5:]  # Exclude the first 5 columns as some are categorical and others are not useful for prediction and can't use win or lose as a feature

#normalize the data using StandardScaler?
#X = (X - X.mean()) / X.std()
X = StandardScaler().fit_transform(X)

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
y_pred = xgb_model.predict(X_test)

# Calculate accuracy score
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

end_time = time.time() 

execution_time = end_time-start_time

print(f"Execution time: {execution_time} seconds")

#save the model as pkl file