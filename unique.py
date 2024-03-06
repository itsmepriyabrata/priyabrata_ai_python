def all_unique(numbers):
     
     if len(numbers)==len(set(numbers)):
          return True
     else:
          return False
print(all_unique([1,2,33,44,5]))
print(all_unique([3,5,6,8]))
