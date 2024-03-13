import numpy as np

# Define sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Set random seed for reproducibility
np.random.seed(42)

# Initialize weights and biases
input_size = 1
hidden_layer_sizes = [6, 6, 6, 6, 6, 6]
output_size = 1

# Initialize weights with random values
weights = [np.random.rand(input_size, hidden_layer_sizes[0])]
biases = [np.zeros((1, hidden_layer_sizes[0]))]

for i in range(1, len(hidden_layer_sizes)):
    weights.append(np.random.rand(hidden_layer_sizes[i-1], hidden_layer_sizes[i]))
    biases.append(np.zeros((1, hidden_layer_sizes[i])))

weights.append(np.random.rand(hidden_layer_sizes[-1], output_size))
biases.append(np.zeros((1, output_size)))

# Training parameters
learning_rate = 0.01
epochs = 10000

# Training data (you can replace this with your own dataset)
X = np.array([[0.5]])  # Input
y = np.array([[0.8]])  # Target output

# Training loop
for epoch in range(epochs):
    # Forward pass
    hidden_layers = [X]
    for i in range(len(hidden_layer_sizes)):
        hidden_layers.append(sigmoid(np.dot(hidden_layers[i], weights[i]) + biases[i]))

    output_layer = sigmoid(np.dot(hidden_layers[-1], weights[-1]) + biases[-1])

    # Backward pass
    error = y - output_layer
    output_delta = error * sigmoid_derivative(output_layer)

    hidden_deltas = [output_delta]
    for i in range(len(hidden_layer_sizes) - 1, 0, -1):
        hidden_delta = np.dot(hidden_deltas[0], weights[i].T) * sigmoid_derivative(hidden_layers[i])
        hidden_deltas.insert(0, hidden_delta)

    # Update weights and biases
    for i in range(len(weights)):
        weights[i] += learning_rate * np.dot(hidden_layers[i].T, hidden_deltas[i])
        biases[i] += learning_rate * np.sum(hidden_deltas[i], axis=0, keepdims=True)

# Test the trained network
test_input = np.array([[0.3]])
predicted_output = sigmoid(np.dot(sigmoid(np.dot(test_input, weights[0]) + biases[0]), weights[1]) + biases[1])
print("Input:", test_input)
print("Predicted Output:", predicted_output)
