class HalfDiamondPattern:
    def __init__(self, size):
        self.size = size

    def print_pattern(self):
        for i in range(self.size):
            for j in range(i + 1):
                print("*", end="")
            print()
        for i in range(self.size - 1, 0, -1):
            for j in range(i):
                print("*", end="")
            print()

# Example usage:
size = 5
pattern = HalfDiamondPattern(size)
pattern.print_pattern()
