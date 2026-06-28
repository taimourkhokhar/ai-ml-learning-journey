#modules
import math
import requests
from colorama import init,Fore,Back,Style
import pyfiglet
import random




init()





print(requests.__version__)
print(math.sqrt(144))
print(math.pi)
print(math.factorial(6))
print(Fore.RED+"Hello")
print(Fore.GREEN+"Hello")
print(Fore.BLUE+"Hello")
# print(Back.BLUE+"hello")
# print(Style.BRIGHT+"hello")


# banner=pyfiglet.figlet_format("Taimour")
# print(banner)


# number1=math.floor(random.random()*10)
# number2=math.floor(random.random()*10)


# def calculator():
#   add=number1+number2
#   return add

# print(calculator())

# user=int(input("Enter a number to guess "))
# if user==calculator():
#   print("True you guess the right number")
# else:
#   print(f"You guess the incorrect number your number is {user} and computer number is {calculator()}")
  
  
  
# with open("student.txt","w") as file:
#   file.write("Ali\n")
#   file.write("Ahmad\n")
#   file.write("Sara\n")
  
# with open("student.txt","r") as file:
#   reader=file.read()

#   print(reader)
  
# user=input("Enter a user name")

# with open("student.txt","a") as file:
#   file.write(f"{user}\n")


# with open ("marks.txt","w") as file:
#   file.write("Ali 80\n")
#   file.write("Ahmad 40\n")
#   file.write("Sara 70\n")


# total=0
# average=0
# count=0  
# with open("marks.txt","r") as file:
  

#   for read in file:
#    parts=read.split()
#    if len(parts)==2:
#     name=parts[0]
#     marks=int(parts[1])
#     total+=marks
#     count+=1
   
# print("Total marks is ",total)
# print("Average is ",total/count)