# # for i in range(1,6):
# #     for j in range(1,i+1):
# #      print("*",end="")
# #     print()

# # for i in range(1, 6):
# #   print("*" * i)

# numbers = [10, 15, 20, 25, 30, 35, 40, 45]
# even=list(filter(lambda x:x%2==0 , numbers))
# square=list(map(lambda x:x**2,numbers))
# greater=list(filter(lambda x:x>25,numbers))
# result=list(sorted(numbers,key=lambda x:x,reverse=True))
# print(result)
# print(greater)
# print(square)
# print(even)

# import math
# print(math.ceil(5.7))

# import random
# ls=["taimour","zaim"]
# print(random.choice(ls))


# import random

# def generate_password(length=12):
#     characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    
#     password = ''.join(random.choices(characters, k=length))
#     return password

# print(generate_password(12))

import json

# st1=input("Enter a name of student 1 :")
# mark1=int(input("Enter marks of student 1"))
# st2=input("Enter a name of student 2 :")
# mark2=int(input("Enter the marks of student 2"))
# students=[
#     {"name":st1,"marks":mark1},
#     {"name":st2,"marks":mark2}
# ]

# with open("student.json","w") as f:
#     json.dump(students,f,indent=2)

# with open("student.json","r") as f:
#     students=json.load(f)
# if students:
#     top_student=max(students,key=lambda s:s["marks"])
#     print(f"Top student: {top_student['name']} with {top_student['marks']} marks")
# else:
#     print("No record found")


# try:
#     number = int(input("Enter a number: "))
#     result = 10 / number

#     print(result)

# except:
#     print("Something went wrong!")

# try:
#     with open("data.txt","r") as f:
#         f.read()
# except FileNotFoundError:
#     print("file not found")
# finally:
#     print("file not found")

# try:
#     starting_balance = 10000
#     withdraw = int(input("Enter how much you want to withdraw: "))

#     if withdraw < 0:
#         raise ValueError("Amount cannot be negative")
#     if withdraw > starting_balance:
#         raise ValueError("Amount exceeds existing balance")

#     remaining_balance = starting_balance - withdraw
#     print(f"Withdrawal successful! Remaining balance: {remaining_balance}")

# except ValueError as e:
#     print("Error:", e)

# class Bank:
#     def __init__(self,holder,balance):
#         self.holder=holder
#         self.balance=balance
#     def deposit(self):
#         dp=int(input("Enter a money "))
#         self.balance+=dp
#         print(self.balance)
# bn=Bank("Taimour",3000)
# bn.deposit()

