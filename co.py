import numpy as np
def calculate_correlation_coefficient(x,y):
      correlation_matrix=np.corrcoef(x,y)
      correlation_coefficient=correlation_matrix[0,1]
      return correlation_coefficient

x=[1,2,3,4,5]
y=[2,4,6,8,10]
result=calculate_correlation_coefficient(x,y)
print(f"the correlation coefficient between x and y is:{result}")
