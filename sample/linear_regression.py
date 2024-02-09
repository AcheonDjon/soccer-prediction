from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def linear_regression_prediction():
    """
    Perform linear regression on the iris dataset and calculate the accuracy score.

    Returns:
    accuracy (float): The accuracy score of the linear regression model.
    """

    # Load the iris dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a LinearRegression model
    model = LinearRegression()

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Calculate the accuracy score
    accuracy = accuracy_score(y_test, y_pred.round())

    return accuracy

accuracy_score = linear_regression_prediction()
print("Accuracy Score:", accuracy_score)