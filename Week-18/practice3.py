# #iterators in python
# number=[1,2,3]
# my_iter=iter(number)
# print(next(my_iter))
# print(next(my_iter))


# class Countdown:
#   """An iterator that control down from starting number to 1"""
#   def __init__(self,start):
#     self.current=start
  
#   def __iter__(self):
#     return self
  
#   def __next__(self):
#     if self.current<=0:
#       raise StopIteration
    
#     data=self.current
#     self.current-=1
#     return data
  
# counter=Countdown(3)
# for num in counter:
#   print(num)

# class PrimeNumber:
#   """An iterator that control just prime number from range 1 to 100"""
#   def __init__(self,start):
#     self.current=start
#     self.max_limit=100

#   def __iter__(self):
#     return self
  
#   def _is_prime(self,n):
#     """Helper method to check if a number is prime"""
#     if n<2:
#       return False
#     for i in range(2, int(n**0.5)+1):
#       if n%i==0:
#         return False
#     return True
  
#   def __next__(self):
#     if self.current>self.max_limit:
#       raise StopIteration
    
#     while self.current<=self.max_limit:
#       data=self.current
#       self.current+=1
#       if self._is_prime(data):
#         return data
#     return StopIteration
  

# counter=PrimeNumber(1)
# for num in counter:
#     print(num)


# name="Taimour"
# my_iter=iter(name)
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))


# class Reverser:
#   """An iterator that show number in reverse order 100 90....."""
#   def __init__(self,start):
#     self.current=start
#   def __iter__(self):
#     return self
#   def __next__(self):
#     if self.current<0:
#       raise StopIteration
#     data=self.current
#     self.current-=10
#     return data
  
# rev=Reverser(100)
# for num in rev:
#   print(num)

# class infiniteColors:
#   """An iterator that loops over a list of colors forever"""
#   def __init__(self,colors):
#     self.colors=colors
#     self.index=0
#   def __iter__(self):
#     return self
#   def __next__(self):
#     color=self.colors[self.index]

#     self.index=(self.index+1)%len(self.colors)
#     return color
  
# color_iterator=infiniteColors(["Red","Green","Blue"])

# for color in color_iterator:
#   print(color)
