import math

class NeuralNetwork:
    def _init_(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Initialize weights and biases
        self.weights_input_hidden = [[0.1] * hidden_size for _ in range(input_size)]
        self.weights_hidden_output = [[0.1] * output_size for _ in range(hidden_size)]

        self.biases_hidden = [0.1] * hidden_size
        self.biases_output = [0.1] * output_size

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def forward(self, inputs):
        # Forward pass
        hidden_input = [sum(i * w for i, w in zip(inputs, col)) + bias for col, bias in zip(zip(*self.weights_input_hidden), self.biases_hidden)]
        hidden_output = [self.sigmoid(x) for x in hidden_input]

        final_input = [sum(h * w for h, w in zip(hidden_output, col)) + bias for col, bias in zip(zip(*self.weights_hidden_output), self.biases_output)]
        final_output = [self.sigmoid(x) for x in final_input]

        return hidden_output, final_output

    def backward(self, inputs, targets, learning_rate):
        # Backward pass
        hidden_output, final_output = self.forward(inputs)

        # Calculate output layer errors and deltas
        output_errors = [target - output for target, output in zip(targets, final_output)]
        output_deltas = [error * self.sigmoid_derivative(output) for error, output in zip(output_errors, final_output)]

        # Update output layer weights and biases
        for i in range(self.hidden_size):
            for j in range(self.output_size):
                self.weights_hidden_output[i][j] += learning_rate * output_deltas[j] * hidden_output[i]
            self.biases_output[j] += learning_rate * output_deltas[j]

        # Calculate hidden layer errors and deltas
        hidden_errors = [sum(w[j] * output_deltas[j] for j in range(self.output_size)) for w in zip(*self.weights_hidden_output)]
        hidden_deltas = [error * self.sigmoid_derivative(output) for error, output in zip(hidden_errors, hidden_output)]

        # Update hidden layer weights and biases
        for i in range(self.input_size):
            for j in range(self.hidden_size):
                self.weights_input_hidden[i][j] += learning_rate * hidden_deltas[j] * inputs[i]
            self.biases_hidden[j] += learning_rate * hidden_deltas[j]

    def train(self, training_data, epochs, learning_rate):
        for epoch in range(epochs):
            for inputs, targets in training_data:
                self.backward(inputs, targets, learning_rate)


# Example usage:
input_size = 2
hidden_size = 3
output_size = 1

# Define a simple XOR dataset
training_data = [([0, 0], [0]),
                 ([0, 1], [1]),
                 ([1, 0], [1]),
                 ([1, 1], [0])]

# Create a neural network
neural_network = NeuralNetwork(input_size, hidden_size, output_size)

# Train the neural network
neural_network.train(training_data, epochs=10000, learning_rate=0.1)

# Test the trained neural network
for inputs, _ in training_data:
    _, prediction = neural_network.forward(inputs)
    print(f"Input: {inputs}, Prediction: {prediction}")
