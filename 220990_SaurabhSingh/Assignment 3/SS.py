# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1468Y1U1EZcDpPqsISS0ly90Gy7IR99Fy
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
#dataset
df = pd.read_csv('/content/winequality-red.csv')
# Creating the column with binary values (0 or 1) for quality check
df['is_good_quality'] = (df['quality'] >= 7).astype(int)

# Drop the original 'quality' column
df.drop('quality', axis=1, inplace=True)

# Data pre-processing steps

# Handling Missing Values (assuming mean imputation)
df.fillna(df.mean(), inplace=True)

# Feature Scaling
scaler = StandardScaler()
df.iloc[:, :-1] = scaler.fit_transform(df.iloc[:, :-1])

# Train-Test Split
X = df.drop('is_good_quality', axis=1)
y = df['is_good_quality']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Logistic Regression
logistic_regression_model = LogisticRegression()
logistic_regression_model.fit(X_train, y_train)
logistic_regression_predictions = logistic_regression_model.predict(X_test)

# K-Nearest Neighbors
k_neighbors_model = KNeighborsClassifier()
k_neighbors_model.fit(X_train, y_train)
k_neighbors_predictions = k_neighbors_model.predict(X_test)

# Decision Trees Classifier
decision_tree_model = DecisionTreeClassifier()
decision_tree_model.fit(X_train, y_train)
decision_tree_predictions = decision_tree_model.predict(X_test)

# Random Forest Classifier
random_forest_model = RandomForestClassifier()
random_forest_model.fit(X_train, y_train)
random_forest_predictions = random_forest_model.predict(X_test)

# Logistic Regression from Scratch
class LogisticRegressionFromScratch:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def fit(self, X, y):
        # Initialize weights and bias
        self.weights = np.zeros(X.shape[1])
        self.bias = 0

        for _ in range(self.n_iterations):
            # Calculate predicted probabilities
            z = np.dot(X, self.weights) + self.bias
            predictions = self.sigmoid(z)

            # Calculate gradients
            dw = (1 / len(y)) * np.dot(X.T, (predictions - y))
            db = (1 / len(y)) * np.sum(predictions - y)

            # Update weights and bias
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    def predict(self, X):
        z = np.dot(X, self.weights) + self.bias
        predictions = self.sigmoid(z)
        return (predictions >= 0.5).astype(int)

# Train Logistic Regression from Scratch
lr_model = LogisticRegressionFromScratch(learning_rate=0.01, n_iterations=1000)
lr_model.fit(X_train.values, y_train.values)
lr_predictions = lr_model.predict(X_test.values)


# Evaluate models
def evaluate_model(model, predictions, algorithm_name):
    accuracy = accuracy_score(y_test, predictions)
    print(f"{algorithm_name} Accuracy: {accuracy:.2f}")
    print(f"{algorithm_name} Classification Report:")
    print(classification_report(y_test, predictions))

# Evaluate Logistic Regression model
evaluate_model(logistic_regression_model, logistic_regression_predictions, "Logistic Regression")

# Evaluate K-Nearest Neighbors model
evaluate_model(k_neighbors_model, k_neighbors_predictions, "K-Nearest Neighbors")

# Evaluate Decision Trees Classifier model
evaluate_model(decision_tree_model, decision_tree_predictions, "Decision Trees Classifier")

# Evaluate Random Forest Classifier model
evaluate_model(random_forest_model, random_forest_predictions, "Random Forest Classifier")

# Evaluate Logistic Regression from Scratch
evaluate_model(lr_model, lr_predictions, "Logistic Regression from scratch")

