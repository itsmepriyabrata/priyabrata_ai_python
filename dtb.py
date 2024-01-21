def decimal_to_binary(decimal):
      binary = bin(decimal)[2:]
      return binary


decimal = 11
binary_result = decimal_to_binary(decimal)
print(f"The binary equivalent of {decimal} is {binary_result}")
