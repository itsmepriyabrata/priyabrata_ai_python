#write a python program on hhow is variance calculated in statistics,and what does it represent
def calculate_variance(data):
       n=len(data)
       mean=sum(data)/n
       squared_diff=[(x-mean)**2 for x in data]
       variance=sum(squared_diff)/n
       return variance

data=[2,3,6,8,10]
result=calculate_variance(data)
print(f"the variance of the data is:{result} ")
            
