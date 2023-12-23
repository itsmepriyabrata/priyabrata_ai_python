
import numpy as np

class NeuronLayer:
    def _init_(self, input_size, num_neurons):
        self.weights = np.random.rand(input_size, num_neurons)
        self.biases = np.zeros(num_neurons)

    def forward(self, inputs):
        return np.dot(inputs, self.weights) + self.biases

# Define three neurons
input_size = 2  # Two input neurons
hidden_neurons = 1  # One hidden neuron
output_neurons = 1  # One output neuron

# Create input layer with two neurons
input_layer = NeuronLayer(input_size, hidden_neurons)

# Create output layer with one neuron
output_layer = NeuronLayer(hidden_neurons, output_neurons)

# Example input data
input_data = np.array([1.0, 2.0])

# Forward pass through the input layer
hidden_layer_output = input_layer.forward(input_data)

# Forward pass through the output layer
final_output = output_layer.forward(hidden_layer_output)

# Display results
print("Input Data:", input_data)
print("Hidden Layer Output:", hidden_layer_output)
print("Final Output:", final_output)
