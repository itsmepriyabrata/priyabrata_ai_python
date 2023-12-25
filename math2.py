import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

def initialize_weights(input_size, hidden_layers, neurons_per_layer, output_size):
    layers = [input_size] + hidden_layers + [output_size]
    weights = []

    for i in range(len(layers) - 1):
        w = np.random.uniform(size=(layers[i], layers[i+1]))
        weights.append(w)

    return weights

def forward_pass(input_data, weights, biases):
    layer_outputs = [input_data]
    for i in range(len(weights)):
        layer_input = np.dot(layer_outputs[-1], weights[i]) + biases[i]
        layer_output = sigmoid(layer_input)
        layer_outputs.append(layer_output)

    return layer_outputs

def backward_pass(layer_outputs, target_output, weights):
    errors = [target_output - layer_outputs[-1]]
    deltas = [errors[-1] * sigmoid_derivative(layer_outputs[-1])]

    for i in range(len(layer_outputs) - 2, 0, -1):
        error = deltas[-1].dot(weights[i].T)
        delta = error * sigmoid_derivative(layer_outputs[i])
        errors.append(error)
        deltas.append(delta)

    return errors[::-1], deltas[::-1]

def update_weights(weights, biases, layer_outputs, deltas, learning_rate):
    for i in range(len(weights)):
        weights[i] += layer_outputs[i].T.dot(deltas[i]) * learning_rate
        biases[i] += np.sum(deltas[i], axis=0, keepdims=True) * learning_rate

def train_neural_network(input_data, target_output, hidden_layers, neurons_per_layer, output_size, learning_rate, epochs):
    input_size = input_data.shape[1]
    weights = initialize_weights(input_size, hidden_layers, neurons_per_layer, output_size)
    biases = [np.zeros((1, neurons)) for neurons in neurons_per_layer + [output_size]]

    for epoch in range(epochs):
        layer_outputs = forward_pass(input_data, weights, biases)
        errors, deltas = backward_pass(layer_outputs, target_output, weights)
        update_weights(weights, biases, layer_outputs, deltas, learning_rate)

    return weights, biases

# Example usage:
input_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
target_output = np.array([[0], [1], [1], [0]])

hidden_layers = [4, 3]  # Define the number of neurons in each hidden layer
neurons_per_layer = hidden_layers
output_size = 1
learning_rate = 0.01
epochs = 10000

trained_weights, trained_biases = train_neural_network(input_data, target_output, hidden_layers, neurons_per_layer, output_size, learning_rate, epochs)

# Testing the trained model
test_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
output = forward_pass(test_data, trained_weights, trained_biases)[-1]

print("Predicted Output after Training:")
print(output)
