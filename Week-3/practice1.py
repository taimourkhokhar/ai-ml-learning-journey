#1 install and use requests
# import requests



# r=requests.get('https://jsonplaceholder.typicode.com/posts')
# data=r.json()
# for index,post in enumerate(data):
#   print(f"{index+1}:{post['title']}")
#   if index==4:
#    break





# from colorama import Fore,Back,Style
# print(Fore.RED+'Error')
# print(Fore.GREEN+"Success")

# password generator 


# import random

# import string

# length=int(input("Enter a password length"))

# characters=string.ascii_letters+string.digits+string.punctuation

# password=''.join(random.choice(characters) for i in range(length))



# print(f"Your new password is: {password}")


#4 convert user name into ASCII art

# import pyfiglet 

# text="Taimour"

# ascii=pyfiglet.figlet_format(text,font="slant")

# print(ascii)




#show current date and time in custom format

# import datetime

# dt=datetime.datetime.now()

# print(dt)



#2 create notes.txt wirte 5 lines into it and then read and print all lines


# f=open("D:notes.txt",'w')
# f.write("Hello my name is Taimour khokhar.\nThis is second line")
# f.close

# f=open("D:notes.txt",'a')
# f.write("\nThis is third line")
# f.close()

# f=open("D:notes.txt",'r')
# read=f.read()
# f.close


# words=read.split()
# words_count=len(words)
# print(words_count)
# lines=read.splitlines()
# lines_count=len(lines)
# print(lines_count)
# print(read)


#create a copy file  program so read from file1.txt and write into file2.txt

# f=open("D:file1.txt",'w')
# f.write("This is from file1")
# f.close

# f=open("D:file1.txt",'r')
# read=f.read()
# f.close

# f=open("D:file2.txt",'w')
# f.write(read)
# f.close



#take use input number handle if enter string instead
# try:
#  user_input=int(input("Enter any number "))
#  print(user_input)
# except ValueError as e:
#  print("Error do with integer",e)


#divide two number handle division by zero and invalid input

# try:
#   n1=int(input("Enter first number "))
#   n2=int(input("Enter second number "))
#   print("Division answer is ",n1/n2)
# except ZeroDivisionError as e:
#   print(e)
# except ValueError as e:
#   print(e)



# try:
#   f=open("D:nots.txt",'r')
#   read=f.read()
#   f.close
#   print(read)
# except FileNotFoundError as e:
#   print("file not found",e)
# finally:
#   print("Runs on both condition")