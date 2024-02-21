class BayesianCalculator:
    def _init_(self, prior_probability):
        self.prior_probability = prior_probability

    def update_multiply(self, likelihood):
        self.prior_probability *= likelihood

    def update_divide(self, likelihood):
        if likelihood != 0:
            self.prior_probability /= likelihood

# Example usage:
# Initialize with a prior probability
calculator = BayesianCalculator(0.5)

# Update with multiplication likelihood
calculator.update_multiply(0.7)

# Update with division likelihood
calculator.update_divide(0.3)

print("Final Probability:", calculator.prior_probability)
