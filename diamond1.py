def print_number_diamond(N):
    # Upper half of the diamond
    for i in range(1, N + 1):
        print((N - i) * " ", end="")
        for j in range(1, i + 1):
            print(j, end="")
            if j != i:
                print("*", end="")
        for j in range(i - 1, 0, -1):
            print(j, end="")
            if j != 1:
                print("*", end="")
        print()

    # Lower half of the diamond
    for i in range(N - 1, 0, -1):
        print((N - i) * " ", end="")
        for j in range(1, i + 1):
            print(j, end="")
            if j != i:
                print("*", end="")
        for j in range(i - 1, 0, -1):
            print(j, end="")
            if j != 1:
                print("*", end="")
        print()

# Example usage:
N = 5
print_number_diamond(N)
