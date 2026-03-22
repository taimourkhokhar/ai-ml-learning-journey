#BAsic iteration Craete an iterator form the list [2,34,6,8,10] and print all elements on by one using the next() function

# nums=[2,4,6,8,10]

# itr=iter(nums)

# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

# class ReverseList:
#   def __init__(self):
#     self.list=[1,2,3,4,5]
#     self.index=len(self.list)

#   def __iter__(self):
#     return self
#   def __next__(self):
#     self.index-=1
#     if self.index<0:
#       raise StopIteration
#     else:
#       return self.list[self.index]
    




# rv=ReverseList()
# itr=iter(rv)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))



#Write a iterator that iterator over a list of numbers and only return even numbers ... 


# class Traverse:
#   def __init__(self,data):
#     self.data=data
#     self.index=0

#   def __iter__(self):
#     return self
  
#   def __next__(self):
#    while self.index<len(self.data):
#     current_value=self.data[self.index]
#     self.index+=1
#     if current_value%2==0:
#       return current_value
#    return StopIteration
  


# data=[1,2,3,4,5,6,7,8,9,10]
# tr=Traverse(data)

# itr=iter(tr)

# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))



# def Custom_remote_Control():
#   yield "CNN"
#   yield "BBC"

# itr=Custom_remote_Control()
# print(next(itr))
# print(next(itr))

#Basic generator function:
#Write a generator function countdown(n) that yields numbers from n down to 1.

# def countdown(n):
#   for i in range(n):
#     yield n-i


# itr=countdown(5)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))




#Write a generator that takes a list and yields only even number

# def even_numbers(lst):
#   for i in lst:
#     if i%2==0:
#      yield i
# list=[2,3,4,5,6]
# itr=even_numbers(list)
# print(next(itr))
# print(next(itr))
# print(next(itr))


# Generator expression:
# Create a generator expression that yields the squares of all odd numbers from 1 to 20.


# def squares():
#   for i in range(1,21):
#     if i%2!=0:
#       yield i*i



# itr=squares()

# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))



