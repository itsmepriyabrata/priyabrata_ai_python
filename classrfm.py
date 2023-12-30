import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class RandomForestModel:
    def _init_(self, n_estimators=100, max_depth=None, random_state=None):
        self.model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=random_state)

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)

    def evaluate(self, X_test, y_test):
        y_pred = self.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        return accuracy

# Example usage
if _name_ == "_main_":
    # Assuming you have a DataFrame 'df' with features and target column
    # For demonstration, let's assume a binary classification problem

    # Sample data creation (replace this with your actual data)
    data = {
        'Feature1': np.random.rand(100),
        'Feature2': np.random.rand(100),
        'Target': np.random.choice([0, 1], size=100)
    }
    df = pd.DataFrame(data)

    # Split the data into features (X) and target variable (y)
    X = df[['Feature1', 'Feature2']]
    y = df['Target']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the Random Forest model
    rf_model = RandomForestModel(random_state=42)
    rf_model.train(X_train, y_train)

    # Evaluate the model
    accuracy = rf_model.evaluate(X_test, y_test)
    print(f"Accuracy: {accuracy}") 
