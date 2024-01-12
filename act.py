import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Generate values from -10 to 10
x_values = np.linspace(-10, 10, 100)

# Apply the sigmoid activation function
y_values = sigmoid(x_values)

# Plot the original values and the activated values
plt.plot(x_values, x_values, label='Original Values')
plt.plot(x_values, y_values, label='Sigmoid Activation')
plt.title('Effect of Sigmoid Activation Function')
plt.xlabel('Input Values')
plt.ylabel('Output Values')
plt.legend()
plt.show()
