# def greet_decorator(func):
#   def wrapper():
#     print("Before greeting")
#     func()
#     print("after greeting")
#   return wrapper



# @greet_decorator
# def say_hello():
#   print("Hello")

# say_hello()

# import time
# def starter(func):
#   def wrapper():
#     print(f"before function {time.time()}")
#     func()
#     print(f"after function{time.time()}")
#   return wrapper

# @starter
# def numbers():
#   for i in range(1,10000):
#     print(i)

# numbers()


# def repeat_twice(func):
#   def wrapper():
#     count=1
#     while count<=2:
#       func()
#       count+=1
#   return wrapper

# @repeat_twice
# def welcome():
#   print("Welcome")

# welcome()

# def changecase(func):
#   def inner(*args,**kwargs):
#     return func(*args,**kwargs)
#   return inner

# @changecase
# def myfunction(name):
#   return "Hello" +name

# print(myfunction("john"))

import threading
import multiprocessing
import time

def d1():
  print("Download file 1")
  time.sleep(2)
  print("Download file 1 completed")

def d2():
  print("Download flie 2")
  time.sleep(2)
  print("Download file 2 completed ")

def d3():
  print("Download file 3")
  time.sleep(3)
  print("Download file 3 completed")

# t1=threading.Thread(target=d1)
# t2=threading.Thread(target=d2)
# t3=threading.Thread(target=d3)
# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()

# if __name__=="__main__":

#  t1=multiprocessing.Process(target=d1)
#  t2=multiprocessing.Process(target=d2)
#  t3=multiprocessing.Process(target=d3)
#  t1.start()
#  t2.start()
#  t3.start()

#  t1.join()
#  t2.join()
#  t3.join()


# import threading

# class BankAccount:
#     def __init__(self, initial_balance):
#         self.balance = initial_balance
#         # Creating a lock to prevent threads from making a mess of the balance simultaneously
#         self.lock = threading.Lock()

#     def deposit(self):
#         for _ in range(100):
#             with self.lock:
#                 self.balance += 10  # Adding 10 to the balance 100 times
#                 print(f"Deposited! Now balance is {self.balance}")

#     def withdraw(self):
#         for _ in range(100):
#             with self.lock:
#                 self.balance -= 10  # Subtracting 10 from the balance 100 times
#                 print(f"Withdrew! Now balance is {self.balance}")

# # 1. Initialize the account
# bk = BankAccount(1000)

# # 2. Pass the method names directly to target WITHOUT parentheses ()
# t1 = threading.Thread(target=bk.deposit)
# t2 = threading.Thread(target=bk.withdraw)

# # 3. Start and join the threads
# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print(f"Final Account Balance: {bk.balance}")


import multiprocessing
import time

def square(n):
  for i in n:
    result=i*i
    print(f"Square of {i} is {result}")

def square1(n):
  for i in n:
    result=i*i
    print(f"square of {i} is {result}")

if __name__=="__main__":
 numbers=[1,2,3,4,5,6,7,8]

 p1=multiprocessing.Process(target=square,args=(numbers,))
 p2=multiprocessing.Process(target=square1,args=(numbers,))
 
 p1.start()
 p1.join()

 p2.start()
 p2.join()