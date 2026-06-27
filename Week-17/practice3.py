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


banner=pyfiglet.figlet_format("Taimour")
print(banner)


number1=math.floor(random.random()*10)
number2=math.floor(random.random()*10)


def calculator():
  add=number1+number2
  return add

print(calculator())

user=int(input("Enter a number to guess "))
if user==calculator():
  print("True you guess the right number")
else:
  print(f"You guess the incorrect number your number is {user} and computer number is {calculator()}")