#write a python program on what is the formula for calculating the mean (average)of a set of numbers
def calculate_mean(numbers):
      if len(numbers)==0:
            return "cannot calculate mean for an empty set"
      mean=sum(numbers)/len(numbers)
      return mean

numbers=[2,4,6,8,10]
result=calculate_mean(numbers)
print(f"the mean of the numbers is :{result}")
      
