import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import xgboost as xgb

class XGBoostModel:
    def _init_(self, params=None):
        if params is None:
            # You can customize the parameters based on your specific problem
            self.params = {
                'objective': 'binary:logistic',
                'max_depth': 3,
                'learning_rate': 0.1,
                'n_estimators': 100,
                'eval_metric': 'logloss'
            }
        else:
            self.params = params

        self.model = xgb.XGBClassifier(**self.params)

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
    # For demonstration, let's use the Titanic dataset

    # Sample data loading (replace this with your actual data)
    # You can download the Titanic dataset from various sources like Kaggle
    # Here, I'm assuming you have a CSV file named 'titanic.csv'
    df = pd.read_csv('titanic.csv')

    # Feature engineering and preprocessing (customize based on your needs)
    # For simplicity, let's consider a few features
    X = df[['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']]
    y = df['Survived']

    # Handling missing values and other preprocessing steps can be added

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the XGBoost model
    xgb_model = XGBoostModel()
    xgb_model.train(X_train, y_train)

    # Evaluate the model
    accuracy = xgb_model.evaluate(X_test, y_test)
    print(f"Accuracy: {accuracy}")
