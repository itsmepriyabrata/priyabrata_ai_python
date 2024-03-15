class BinaryDecimalConverter:
    
    def binary_to_decimal(binary_str):
        decimal_num = int(binary_str, 2)
        return decimal_num

    @staticmethod
    def decimal_to_binary(decimal_num):
        binary_str = bin(decimal_num)[2:]
        return binary_str

# Example usage:
binary_input = "1101"
decimal_output = BinaryDecimalConverter.binary_to_decimal(binary_input)
print(f"Binary: {binary_input} => Decimal: {decimal_output}")

decimal_input = 13
binary_output = BinaryDecimalConverter.decimal_to_binary(decimal_input)
print(f"Decimal: {decimal_input} => Binary: {binary_output}")
