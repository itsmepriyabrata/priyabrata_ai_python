def gradient_descent(x, learning_rate, epochs):
    for epoch in range(epochs):
        gradient = 2 * x  # Example gradient for illustration purposes
        x = x - learning_rate * gradient
        print(f"Epoch {epoch + 1}: x = {x}")

# Example usage:
initial_x = 5
learning_rate = 0.1
num_epochs = 5

gradient_descent(initial_x, learning_rate, num_epochs)
