# nums=[0,0,0,1,1,1]
# index=0

# for i in range(len(nums)):
#   if nums[i]!=0:
#     print(nums[i])
#     nums[index],nums[i]=nums[i],nums[index]

#     index=index+1
# print(nums)

# import numpy as np

# vl=np.array([[1,2,3,4,5],[5,6,7,8,9]],dtype=int)

# print(vl.ndim)
# print(vl.shape)

# print(vl.size)

# nums=[0,1,0,3,12]
# index=0

# for i in range(len(nums)):
#   if nums[i]!=0:# 
#     temp=nums[i]
#     nums[i]=nums[index]
#     nums[index]=temp
#     print(nums[i])
#     index+=1
# print(nums)

# num=5
# class counter:
#   def __init__(self,num) -> None:
#     self.num=num
#     self.count=1
#   def __iter__(self):
#     return self
#   def __next__(self):
#     if self.count<=self.num:
#      res=self.count
#      self.count+=1
#      return res
#     else:
#        raise StopIteration





# my_counter=counter(num)
# for i in my_counter:
#   print(i)




# ls=[10,20,30,40]

# my=iter(ls)

# print(next(my))

#Write a generator that yields numbers from 1 to 10.

# def count(n):
#   count=1
#   while count<=n:
#     yield count
#     count+=1
# gen=count(5)
# print(next(gen))


# def square(n):
#   start=1
#   while start<=n:
#     yield start*start
#     start+=1
# gen=square(10)

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))