import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

def neural_network(input_data):
    
    input_layer_neurons = len(input_data[0])
    hidden_layer_neurons = 4
    output_layer_neurons = 1

    np.random.seed(1)
    weights_input_hidden = 2 * np.random.random((input_layer_neurons, hidden_layer_neurons)) - 1
    weights_hidden_output = 2 * np.random.random((hidden_layer_neurons, output_layer_neurons)) - 1

    for epoch in range(10000):
        input_layer_output = sigmoid(np.dot(input_data, weights_input_hidden))
        hidden_layer_output = sigmoid(np.dot(input_layer_output, weights_hidden_output))

        output_error = target_output - hidden_layer_output
        output_delta = output_error * sigmoid_derivative(hidden_layer_output)

        hidden_layer_error = output_delta.dot(weights_hidden_output.T)
        hidden_layer_delta = hidden_layer_error * sigmoid_derivative(input_layer_output)

        weights_hidden_output += input_layer_output.T.dot(output_delta)
        weights_input_hidden += input_data.T.dot(hidden_layer_delta)

    return hidden_layer_output

input_data = np.array([[0, 0],
                       [0, 1],
                       [1, 0],
                       [1, 1]])

target_output = np.array([[0], [1], [1], [0]])

result = neural_network(input_data)

print("Result after training:")
print(result)
