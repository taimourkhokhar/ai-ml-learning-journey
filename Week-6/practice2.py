#Write a program to read a file and count number of words.

# with open("D:/ai engineer roadmap/funny.txt",'r') as f:
#    vl=f.read()
#    lines=vl.splitlines()
#    print(lines)
#    for line in lines:
#       if 'jennifer' in line:
#          print(line)

# num=int (input("Enter a number1 "))
# num2=int(input("Enter a number 2"))

# try:
#   result=num/num2
#   print(result)
# except ZeroDivisionError as e:
#   print(e)

# try:
#   user=int(input("Enter a integer"))

#   print(user)
# except ValueError as e:
#   print("please input integer",e)

# try:
#   user=int(input("Enter a integer"))
#   print(user)
# except ValueError as e:
#   print(e)
# else:
#   print("do nothing")
# finally:
#   print("run in both")


# try:
#    with open("D:/ai engineer roadmap/funnytxt",'r') as f:
#     f.read()
#     print(f)
# except FileNotFoundError as e:
#   print(e)


# class student:
#   def __init__(self,name,marks):
#     self.name=name
#     self.marks=marks
#   def display_info(self):
#     print(f"name and marks of student is {self.name} {self.marks} ")


# st=student("taimour",33)
# st.display_info()

# class calculator:
#   def __init__(self,num1,num2):
#     self.num1=num1
#     self.num2=num2
#   def addition(self):
#     print(self.num1+self.num2)
#   def subtract(self):
#     print(self.num1-self.num2)

# st=calculator(4,4)
# st.addition()
# st.subtract()
# try:
#     num = int(input("Enter a number: "))
    
#     if num < 0:
#         raise Exception("Number is negative!")   # custom error

#     print("Valid number:", num)

# except Exception as e:
#     print("Error:", e)