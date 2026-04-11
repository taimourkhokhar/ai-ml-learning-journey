# student={
#   "name":"taimour",
#   "age":22,
#   "marks":80,
#   "new":{
#     "address":"lahore"
#   }
# }

# student["grade"]="A-"
# student["marks"]="88"
# print(student)
# print(student["age"],student["name"],student["marks"])

# print(student["new"]["address"])
# for i in student:
#   print(i)
# for val in student.values():
#   print(val)

# for key,val in student.items():
#   print(student["new"])


#create a set and add 3 new element

# new={1,2,3,4,5}
# new.remove(5)
# print(new)

#convert a list with duplicates into a set

# ls=[1,2,2,3]

# ss=set(ls)

# print(ss)



#tuples create a tuple and print its element


# tp=(1,2,3,3,4)
# # print(tp)

# # print(tp[0],tp[-1])

# # for i in tp:
# #   print(tp.count(i))

# print(tp.index(4))

# s="  hello world "
# word=s.split()

# ls=list(word)

# ls.reverse()

# new=" ".join(ls)

# print(new)


# text = "Python is  versatile and   powerful"
# word_count = text.split()
# print(word_count)  # Output: 5

# for i in word_count:
  
# Write a function is_palindrome(s) that checks if a string is palindrome (ignore spaces & case)

# def palindrome(str):
#   new=list(str)
#   new.reverse()
#   ch="".join(new)
#   if str==ch:
#    print("String is palindrome")
#   else:
#     print("No")
# str=input("Enter a string")
# palindrome(str)

# def maxmin(arr):
#   max=arr[0]
#   min=arr[0]
#   for i in arr:
#     if i>max:
#       max=i
#     if i<min:
#       min=i
#   print("Max and Min are",max,min)

# maxmin([1,2,3,4,5])

def fib(n):
  n1,n2=0,1
  count=0
  if n<=0:
    print("Enter a positive integer")
  elif n==1:
    print(n1)
  else:
    print("Fibonacci series")
    while count<n:
      print(n1,end=" ")
      nth=n1+n2 #it has 0+1==1

      n1=n2##here 0==1
      n2=nth
      count+=1
    
# fib(20)
# def fibb(n):
#   a,b=0,1
#   for i in range(n):
#     print(a,end=" ")
#     a,b=b,a+b #0,1=1,0+1 in next a will 1,1=1,2 fur 2,1=2,3
# fibb(20)


# def fibb(n):
#   first,second=0,1
#   for _ in range(n):
#     print(first,end=" ")

#     next_num=first+second#1
#     first=second # now 0 becme 1
#     second=next_num# now second will have next value

# fibb(10)

# dic={
#   "name":"Taimour",
#   "score":{
#     "new":22
#   }
# }

# print(dic["score"]['new'])

# def merge_dicts(d1, d2):

#     result = d1.copy()
    
#     for key, value in d2.items():
#         if key in result:
#             result[key] += value
#         else:
#             result[key] = value
            
#     return result
# dict_a = {'apples': 5, 'oranges': 2}
# dict_b = {'apples': 3, 'bananas': 10}
# print(merge_dicts(dict_a, dict_b))

#2 use lamda with map() to square all numbers in a list

# ls=[1,2,3,4,5]

# new=list(map(lambda x:x*x,ls))
# print(new)

#Use lambda with filter() to get even numbers from a list.

# ls=[1,2,3,4,5]
# nw=list(filter(lambda x:x%2==0,ls))

# print(nw)

# ls=[(1,5),(2,3),(4,1)]

# new=list(sorted(ls,key=lambda x:x[1]))

# print(new)

# n1=10

# new=lambda x : 'high' if x >10 else 'low'

# print(new(n1))

# ls=['taimour','asad','jimmy']

# new=sorted(ls,key=lambda x:len(x))

# print(new)

# names = ["Taimour", "Asad", "Jimmy"]

# new=sorted(names,key=lambda x:x[-1])

# print(new)

# prices = [25, 60, 10, 105, 45, 80]

# nw=list(filter(lambda x:x>50,prices))
# print(nw)

# products = [
#     {"name": "Laptop", "price": 1200},
#     {"name": "Mouse", "price": 25},
#     {"name": "Monitor", "price": 300}
# ]

# new=sorted(products,key=lambda x:x['price'])
# print(new)


# import math

# print(math.sqrt(5))
# print(math.factorial(5))

# import random

# print(random.random())

# ls=[1,2,3,4]

# print(random.choices(ls))

# import datetime

# now=datetime.datetime.now()
# print(now)

# import requests

# now=requests.get('https://dummyjson.com/test')

# print(now.status_code)
