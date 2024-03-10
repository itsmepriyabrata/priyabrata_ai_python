# def array_sum(arr):
#     return sum(arr)
# array=[1,2,3,4,5]
# print("sum of the array:",array_sum(array))

# def find_largest(arr):
#     if not arr:
#         return None
#     max_elem=arr[0]
#     for num in arr:
#         if num>max_elem:
#             max_elem=num
#     return max_elem
# array=[10,2,67,23,40]
# largest=find_largest(array)
# print("the largest element in the array is:",largest)
# class ArrayRotation:
#     def __init__(self,arr):
#         self.arr=arr
#     def rotate_left(self,d):
#         n=len(self.arr)
#         d=d%n
#         self.arr=self.arr[d:]+self.arr[:d]
#     def rotate_right(self,d):
#         n=len(self.arr)
#         d=d%n
#         self.arr=self.arr[-d:]+self.arr[:-d]
#     def get_array(self):
#         return self.arr
# arr=[2,3,44,55,66]
# rotation=ArrayRotation(arr)
# print("original array:",rotation.get_array())
# rotation.rotate_left(2)
# print("after left rotation:",rotation.get_array())
# rotation.rotate_right(1)
# print("after right rotation: ",rotation.get_array())

# class ListInterchanger:
#     def __init__(self,lst):
#         self.lst=lst
#     def interchange_first_last(self):
#         if len(self.lst)>=2:
#             self.lst[0],self.lst[-1]=self.lst[-1],self.lst[0]
#             return self.lst
# my_list=[1,23,3,4,44]
# interchanger=ListInterchanger(my_list)
# interchanged_list=interchanger.interchange_first_last()
# print("interchanged list",interchanged_list)
# class listswapper:
#     def __init__(self,lst):
#         self.lst=lst
#     def swap_elements(self,index1,index2):
#         if 0<=index1<len(self.lst) and 0<=index2<len(self.lst):
#             self.lst[index1],self.lst[index2]=self.lst[index2],self.lst[index1]
#         else:
#             print("error:index out of range")

# my_list=[1,2,23,3,2]
# swapper=listswapper(my_list)
# swapper.swap_elements(1,3)
# print("swapped list:",my_list)

# def print_positive_num(lst):
#     positive_num=[num for num in lst if num > 0]
#     print("positive numbers in the list:",positive_num)

# my_list=[1,2,3,3,4,556,66]
# print_positive_num(my_list)

# list1=[11,2,23,3,445,5]
# for ele in list1:
#     if ele %2 == 0:
#         list1.remove(ele)
# print("new list after removing")

# test_list=[3,3,4,44,55,6]
# print("the original list is :" + str )

 
