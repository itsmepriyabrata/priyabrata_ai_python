import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def binary_classification_decision(probability, threshold=0.5):
    return 1 if probability >= threshold else 0

# Example usage:
input_value = 2.0

# Applying sigmoid to get a probability between 0 and 1
probability = sigmoid(input_value)
print(f"Probability: {probability}")

# Making a binary decision based on the probability and a threshold (default is 0.5)
decision = binary_classification_decision(probability)
print(f"Binary Decision: {decision}")
