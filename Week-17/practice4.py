# with open("name.txt","w") as file:
#   file.write("Hello everyone welcome to Python")

# count=0  
# with open("name.txt","r") as file:
#   read=file.read()
#   for rd in read.split():
#     count+=1
    
# print(count)

 ##simple notes application
# import sys


# def add_note():
#  with open("Add.txt","w") as file:
#   user_input=input("Enter note ")
#   file.write(f"{user_input}\n")
# def view_note():
#  with open("Add.txt","r") as file:
#   reader=file.read()
#   print(reader)

# while True:
#  print("1. Add note")
#  print("2. View note")
#  print("3. Exit")

#  try:
#   user=int(input("Enter your task number "))
#   if user==1:
#    add_note()
#   elif user==2:
#    view_note()
#   elif user==3:
#    sys.exit()
#   else:
#    print("You input a wrong number. Please try a number between 1 and 3")


#  except ValueError:
#     print("Invalid input. Please input a valid number")

#exception handling 

# try:
#   num1=10
#   num2=0
#   final=num1/num2
#   print(final)
# except ZeroDivisionError as e:
#   print("Division by zero error",e)

# try:
#   user=int(input("Enter your age"))
#   print(user)
# except ValueError as e:
#   print(e)
# try:
#  with open("data.txt","r") as file:
#   reader=file.read()
#   print(reader)
# except FileNotFoundError as e:
#  print(e)

# fruits=["apple","banana","orange","pomegranate"]
# try:
#   user=int(input("Enter index "))
#   print(fruits[user])
# except IndexError as e:
#   print(e)

# def addition(a,b):
#   try:
#     final=a+b
#     print("The result of addition is ",final)
#   except ValueError as e:
#     print(e)
# def subtraction(a,b):
#     try:
#      final=a-b
#      print("The result of Subtraction is ",final)
#     except ValueError as e:
#      print(e)

# def multiplication(a,b):
#   try:
#     final=a*b
#     print("The result of multiplication is ",final)
#   except ValueError as e:
#     print(e)

# def division(a,b):
#   try:
#     final=a/b
#     print("The result of divison is ",final)

#   except ZeroDivisionError as e:
#     print(e)




# while True:
#   print("1. Addition")
#   print("2. Subtraction")
#   print("3. Multiplication")
#   print("4. Division")
#   user=int(input("Enter operation number "))
#   a=int(input("Enter first number"))
#   b=int(input("Enter second number"))
#   try:
#     if user==1:
#       addition(a,b)
#     elif user==2:
#       subtraction(a,b)
#     elif user==3:
#       multiplication(a,b)
#     elif user==4:
#       division(a,b)
#     else:
#       print("Please enter a valid number")

#   except ValueError as e:
#     print(e)