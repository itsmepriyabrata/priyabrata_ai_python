import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Input data
input_data = np.array([[0, 0],
                       [0, 1],
                       [1, 0],
                       [1, 1]])

# Target output
target_output = np.array([[0], [1], [1], [0]])

# Set parameters
input_size = 2
hidden_layer_size = 4
output_size = 1
learning_rate = 0.01
epochs = 10000

# Initialize weights and biases
weights_input_hidden = np.random.uniform(size=(input_size, hidden_layer_size))
weights_hidden_output = np.random.uniform(size=(hidden_layer_size, output_size))

bias_hidden = np.zeros((1, hidden_layer_size))
bias_output = np.zeros((1, output_size))

# Training the model
for epoch in range(epochs):
    # Forward pass
    hidden_layer_input = np.dot(input_data, weights_input_hidden) + bias_hidden
    hidden_layer_output = sigmoid(hidden_layer_input)

    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
    predicted_output = sigmoid(output_layer_input)

    # Calculate errors
    error = target_output - predicted_output

    # Backpropagation
    output_delta = error * sigmoid_derivative(predicted_output)
    hidden_layer_error = output_delta.dot(weights_hidden_output.T)
    hidden_layer_delta = hidden_layer_error * sigmoid_derivative(hidden_layer_output)

    # Update weights and biases
    weights_hidden_output += hidden_layer_output.T.dot(output_delta) * learning_rate
    weights_input_hidden += input_data.T.dot(hidden_layer_delta) * learning_rate

    bias_output += np.sum(output_delta, axis=0, keepdims=True) * learning_rate
    bias_hidden += np.sum(hidden_layer_delta, axis=0, keepdims=True) * learning_rate

# Testing the model
test_data = np.array([[0, 0],
                      [0, 1],
                      [1, 0],
                      [1, 1]])

hidden_layer_input_test = np.dot(test_data, weights_input_hidden) + bias_hidden
hidden_layer_output_test = sigmoid(hidden_layer_input_test)

output_layer_input_test = np.dot(hidden_layer_output_test, weights_hidden_output) + bias_output
predicted_output_test = sigmoid(output_layer_input_test)

print("Predicted Output after Training:")
print(predicted_output_test)
