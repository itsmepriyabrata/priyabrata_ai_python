#write a python program on what is the diff between classification and regression in supervised learning
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import accuracy_score, mean_squared_error

# Classification Example
def classification_example():
    # Generate synthetic data for classification
    X_classification = [[1.2], [2.4], [3.1], [4.8], [5.2]]
    y_classification = [0, 0, 1, 1, 1]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_classification, y_classification, test_size=0.2, random_state=42)

    # Create a Logistic Regression model for classification
    model_classification = LogisticRegression()
    model_classification.fit(X_train, y_train)

    # Make predictions on the test set
    predictions = model_classification.predict(X_test)

    # Calculate and print the accuracy
    accuracy = accuracy_score(y_test, predictions)
    print(f"Accuracy in classification: {accuracy}")

# Regression Example
def regression_example():
    # Generate synthetic data for regression
    X_regression = [[1.2], [2.4], [3.1], [4.8], [5.2]]
    y_regression = [2.3, 4.1, 3.9, 6.2, 5.8]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_regression, y_regression, test_size=0.2, random_state=42)

    # Create a Linear Regression model for regression
    model_regression = LinearRegression()
    model_regression.fit(X_train, y_train)

    # Make predictions on the test set
    predictions = model_regression.predict(X_test)

    # Calculate and print the mean squared error
    mse = mean_squared_error(y_test, predictions)
    print(f"Mean Squared Error in regression: {mse}")

# Run the examples
classification_example()
regression_example()
