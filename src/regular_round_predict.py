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
        return 0
    elif row['HomeScore'] == row['AwayScore']:
           if row['Home_xG'] >= row['Away_xG']:
              return 0 #home win        
           else:
              return 1 #away win
    else:
        return 1


# Load the dataset
file_path = './data/regular.csv'
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
model = xgboost.XGBClassifier()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")


print(model.feature_importances_)
