import concurrent.futures

def parallel_addition(num1, num2):
    return num1 + num2

def parallel_multiplication(num1, num2):
    return num1 * num2

if __name__ == "__main__":
    # Input
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))

    # Parallel Execution
    with concurrent.futures.ThreadPoolExecutor() as executor:
        addition_future = executor.submit(parallel_addition, num1, num2)
        multiplication_future = executor.submit(parallel_multiplication, num1, num2)

        # Get results
        result_addition = addition_future.result()
        result_multiplication = multiplication_future.result()

    # Output results
    print(f"Parallel Addition Result: {result_addition}")
    print(f"Parallel Multiplication Result: {result_multiplication}")
