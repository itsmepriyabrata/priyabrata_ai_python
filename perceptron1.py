class Neuron:
    def _init_(self, bias=0):
        self.bias = bias
        self.weights = []

    def add_input(self, neuron, weight):
        self.weights.append((neuron, weight))

    def calculate_output(self):
        total_input = sum(neuron.calculate_output() * weight for neuron, weight in self.weights)
        return self.activation_function(total_input + self.bias)

    def activation_function(self, x):
        # You can define your activation function here, for example, a simple step function
        return 1 if x > 0 else 0


# Creating three neurons
neuron1 = Neuron()
neuron2 = Neuron()
output_neuron = Neuron()

# Connecting neurons
output_neuron.add_input(neuron1, 0.5)
output_neuron.add_input(neuron2, -0.5)

# Calculating the output of the network
result = output_neuron.calculate_output()

print("Output:", result)
