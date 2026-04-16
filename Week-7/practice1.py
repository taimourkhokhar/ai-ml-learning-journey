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

# s = "axc"
# t = "ahbgdc"

# length=max(len(s),len(t))
# i=0
# def check(s,t):
#  for i in range(len(s)):
#    if s[i] not in t:
#     i=i+1
#     return False

#  return True
 

# nums=[1,2,3,4,5,6]
# new=[x*2 for x in nums  if x%2==0]
# print(new)


# words = ["apple", "banana", "cherry", "kiwi"]

# new=[x for x in words if len(x)>5]

# print(new)

# new=[x for x in range(10) if x%3!=0]
# print(new)

# def outer(func):
#   def wrapper(*args,**kwargs):
#      print("Started")
#      result=func(*args,**kwargs)
#      print("Function ended")
#      return result
#   return wrapper

# @outer
# def hello():
#    print("hello")

# hello()

# def outer(func):
#   def inner(num):
#     if num<0:
#      return "Invalid input"
#     return func(num)
#   return inner

# num=-1
# @outer
# def caller(num):
#   return "hello"+str(num)

# print(caller(num))

# import time

# def outer(func):
#   def wrapper(*args,**kwargs):
#     start=time.time()
#     result=func(*args,**kwargs)
#     end=time.time()
#     print(f"total time is {(end)-(start)*1000} s")
#     return result
#   return wrapper

# @outer

# def looper(n):
#   for i in range(1,n):
#     print(i*i)


# looper(1000)

# new={val:val*val for val in range(1,6) }
# print(new)

# words = ["apple", "banana", "cherry"]


# new={val:len(val) for  val in words}

# print(new)

# dic={}

# for i in words:
#   dic[i]=len(i)
# print(dic)

# nums = [1, 2, 3, 4, 5]

# new={val:val*val*val for val in nums if val%2==0}

# print(new)


# new={x*x for x in range(1,10)}
# print(type(new))

# nums = [1, 2, 2, 3, 4, 4, 5]

# new={x*10 for x in nums}

# print(new)

# text = "programming"

# new={x for x in text if x in 'aeiou'}

# print(new)

# nums = [1, 2, 3, 4, 5]

# new=tuple(x for x in nums if x%2==0)

# print(new)

# users = [
#     {"name": "Ali", "age": 20},
#     {"name": "Sara", "age": 17},
#     {"name": "Ahmed", "age": 25}
# ]

# new={val['name']:'adult' if val["age"]>18 else 'minor' for val in users}

# print(new)