def simple_neural_network(input1, input2, weight1, weight2, bias):
    
    weighted_sum = (input1 * weight1) + (input2 * weight2)

    output_neuron = 1 if weighted_sum + bias > 0 else 0

    return output_neuron

neuron_input1 = 0.8
neuron_input2 = 0.4
neuron_weight1 = 0.5
neuron_weight2 = 0.7
neuron_bias = -0.3

output = simple_neural_network(neuron_input1, neuron_input2, neuron_weight1, neuron_weight2, neuron_bias)

print("Output neuron:", output
