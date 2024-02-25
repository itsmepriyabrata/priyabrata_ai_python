import numpy as np
import pandas as pd

class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def read_data(self):
        self.data = pd.read_csv(self.file_path)

    def print_head(self):
        print(self.data.head())

    def unique_values(self, column_name):
        return self.data[column_name].unique()

    def value_counts(self, column_name):
        return self.data[column_name].value_counts()

    def one_hot_encode(self, columns_to_encode):
        return pd.get_dummies(self.data, columns=columns_to_encode)

# Example usage:
file_path = 'C:\\Users\\priyabrata\\Desktop\\scrapping\\myvenv\\hve.csv'
data_processor = DataProcessor(file_path)
data_processor.read_data()

print("Head of the data:")
data_processor.print_head()

print("\nUnique values in 'Gender' column:")
print(data_processor.unique_values('Gender'))

print("\nUnique values in 'Remarks' column:")
print(data_processor.unique_values('Remarks'))

print("\nUnique values in 'work' column:")
print(data_processor.unique_values('work'))

print("\nValue counts for 'Gender' column:")
print(data_processor.value_counts('Gender'))

print("\nValue counts for 'Remarks' column:")
print(data_processor.value_counts('Remarks'))

print("\nValue counts for 'work' column:")
print(data_processor.value_counts('work'))

# One-hot encode specified columns
columns_to_encode = ['Remarks', 'Gender', 'work']
one_hot_encoded_data = data_processor.one_hot_encode(columns_to_encode)
print("\nOne-hot encoded data:")
print(one_hot_encoded_data)
