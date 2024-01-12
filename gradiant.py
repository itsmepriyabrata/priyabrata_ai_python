import numpy as np

def calculate_gradient(f, params):
    epsilon = 1e-5
    gradient = np.zeros_like(params)

    for i in range(len(params)):
        params_plus_epsilon = params.copy()
        params_plus_epsilon[i] += epsilon
        gradient[i] = (f(params_plus_epsilon) - f(params)) / epsilon

    return gradient

# Example usage:
def example_function(params):
    # Example function: f(x, y) = x^2 + 2y^2
    return params[0]*2 + 2 * params[1]*2

initial_params = np.array([1.0, 2.0])
result_gradient = calculate_gradient(example_function, initial_params)

print(f"The gradient of the example function at {initial_params} is: {result_gradient}")
