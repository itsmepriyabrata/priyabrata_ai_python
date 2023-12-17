import numpy as np

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Neural network parameters
input_size = 3  # Number of input features
output_size = 1  # Number of neurons in the output layer

# Initialize weights and bias
weights = np.random.rand(input_size, output_size)
bias = np.random.rand(1)

# Input data
input_data = np.array([[0.2, 0.4, 0.7]])

# Forward pass
weighted_sum = np.dot(input_data, weights) + bias
output = sigmoid(weighted_sum)

# Display results
print("Input Data:")
print(input_data)

print("\nWeights:")
print(weights)

print("\nBias:")
print(bias)

print("\nWeighted Sum:")
print(weighted_sum)

print("\nOutput:")
print(output)
