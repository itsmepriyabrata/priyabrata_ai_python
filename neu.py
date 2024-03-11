import numpy as np
class NeuralNetwork:
    def __init__(self,input_size,hidden_layer_sizes,output_size):
        self.input_size=input_size
        self.hidden_layer_sizes=hidden_layer_sizes
        self.output_size=output_size
        self.weights=[]
        self.biases=[]
        np.random.seed(42)
        layer_sizes=[input_size]+hidden_layer_sizes[output_size]
        for i in range(len(layer_sizes)-1):
            self.weights.append(np.random.rand(layer_sizes[i],layer_sizes[i+1]))
            self.biases.append(np.zeros((1,layer_sizes[i+1])))


def sigmoid(self,x):
    return 1/(1+np.exp(-x))
def sigmoid_derivative(self,x):
    return x*(1-x)
def forward_pass(self,X):
    hidden_layers=[X]
    for i in range(len(self.weights)):
        hidden_layers.append(self.sigmoid(np.dot(hidden_layers[i],self.weights[i]+self.biases[i])))
    return hidden_layers
def backward_pass(self,X,y,hidden_layers):
    error=y-hidden_layers[-1]
    output_delta=error*self.sigmoid_derivative(hidden_layers[-1])
    hidden_deltas=[output_delta]
    for i in range(len(self.weights)-1,0,-1):
        hidden_delta=np.dot(hidden_deltas[0],self.weights[i]*self.sigmoid_derivative(hidden_layers[i]))
        hidden_deltas.insert(0,hidden_delta)
    for i in range(len(self.weights)-1,0,-1):
        hidden_delta=np.dot(hidden_deltas[0],self.weights[i].T)* self.sigmoid_deivative(hidden_layers[i])
        hidden_deltas.insert(0,hidden_deltas)
