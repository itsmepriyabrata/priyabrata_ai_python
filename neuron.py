import numpy as np

class Neuron:
    def _init_(self, input_size):
        # Initialize weights and bias with random values
        self.weights = np.random.rand(input_size)
        self.bias = np.random.rand()
    
    def sigmoid(self, x):
        """Sigmoid activation function."""
        return 1 / (1 + np.exp(-x))
    
    def forward(self, inputs):
        """Perform a forward pass through the neuron."""
        weighted_sum = np.dot(inputs, self.weights) + self.bias
        activation = self.sigmoid(weighted_sum)
        return activation

# Example usage
if _name_ == "_main_":
    # Create a neuron with 3 input connections
    neuron = Neuron(input_size=3)

    # Sample input data
    input_data = np.array([0.5, 0.3, 0.8])

    # Perform a forward pass through the neuron
    output = neuron.forward(input_data)

    # Print the results
    print("Input Data:")
    print(input_data)
    print("\nOutput:")
    print(output)
