import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def initialize_weights(input_size, hidden_size, output_size):
    weights_input_hidden = np.random.uniform(size=(input_size, hidden_size))
    weights_hidden_hidden = np.random.uniform(size=(hidden_size, hidden_size))
    weights_hidden_output = np.random.uniform(size=(hidden_size, output_size))

    biases_hidden = np.zeros((1, hidden_size))
    biases_output = np.zeros((1, output_size))

    return weights_input_hidden, weights_hidden_hidden, weights_hidden_output, biases_hidden, biases_output

def forward_pass(input_data, weights_input_hidden, weights_hidden_hidden, weights_hidden_output, biases_hidden, biases_output):
    hidden_states = [np.zeros((1, weights_hidden_hidden.shape[0]))]
    outputs = []

    for timestep in range(input_data.shape[0]):
        hidden_state = sigmoid(np.dot(input_data[timestep], weights_input_hidden) +
                               np.dot(hidden_states[-1], weights_hidden_hidden) + biases_hidden)
        output = sigmoid(np.dot(hidden_state, weights_hidden_output) + biases_output)

        hidden_states.append(hidden_state)
        outputs.append(output)

    return outputs, hidden_states

# Example usage:
input_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
target_output = np.array([[0], [1], [1], [0]])

input_size = input_data.shape[1]
hidden_size = 4
output_size = 1
learning_rate = 0.01
epochs = 10000

weights_input_hidden, weights_hidden_hidden, weights_hidden_output, biases_hidden, biases_output = initialize_weights(input_size, hidden_size, output_size)

for epoch in range(epochs):
    total_loss = 0
    hidden_states = [np.zeros((1, hidden_size))]

    for timestep in range(input_data.shape[0]):
        # Forward pass
        hidden_state = sigmoid(np.dot(input_data[timestep], weights_input_hidden) +
                               np.dot(hidden_states[-1], weights_hidden_hidden) + biases_hidden)
        output = sigmoid(np.dot(hidden_state, weights_hidden_output) + biases_output)

        # Calculate loss
        loss = 0.5 * np.sum((output - target_output[timestep]) ** 2)
        total_loss += loss

        # Backpropagation (omitted for brevity as we focus on weights reuse)

        # Update hidden states for the next timestep
        hidden_states.append(hidden_state)

    # Update weights (omitted for brevity as we focus on weights reuse)

    # Print loss for monitoring training progress
    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Loss: {total_loss}")

# Testing the trained model
test_outputs, _ = forward_pass(input_data, weights_input_hidden, weights_hidden_hidden, weights_hidden_output, biases_hidden, biases_output)

print("\nPredicted Output after Training:")
print(test_outputs)
