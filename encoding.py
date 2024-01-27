import numpy as np 
import pandas as pd 

try:
    data = pd.read_csv('C:\\Users\\priyabrata\\Desktop\\scrapping\\myvenv\\hve.csv')
except FileNotFoundError:
    print("File not found. Please check the file path.")
    # You might want to exit or handle the error in an appropriate way.
    exit()
print(data['Gender'].value_counts())
print(data['Remarks'].value_counts())
print(data['work'].value_counts())
