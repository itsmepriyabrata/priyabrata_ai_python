def activate(inputs):
    # Sum the inputs and apply a basic activation function (e.g., step function)
    return 1 if sum(inputs) > 0 else 0

def neural_network(input_neurons):
    # Define weights and bias (for simplicity, using hardcoded values)
    weights = [0.5, -0.5]
    bias = 0.2

    # Calculate the weighted sum of inputs and apply activation function
    weighted_sum = sum(w * x for w, x in zip(weights, input_neurons)) + bias
    output = activate(weighted_sum)

    return output

input_neurons = [0.8, 0.4]
output_neuron = neural_network(input_neurons)

print("Input Neurons:", input_neurons)
print("Output Neuron:", output_neuron
