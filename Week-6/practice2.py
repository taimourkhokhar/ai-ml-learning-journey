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

# nums = [1, 2, 3, 4]

# nums=[0,0,0,1,1,1]
# index=0

# for i in range(len(nums)):#6
#   if nums[i]!=0:#
#     temp=nums[i]#here temp has 1 1 1 
#     nums[i]=nums[index]# here 1 1 1 is put at 0 index
#     nums[index]=temp#here at 0 index 1 1 1 put
#     index+=1

# print(nums)



# nums = [1,2,0,0,5]
# def passe(nums):
#  small=float('inf')
#  mid=float('inf')
#  third=float('inf')
#  print(third)
#  for i in nums:
#   if i<=small:
#    small=i #here small has 1
#   elif i<=mid:
#    mid=i#here mid has 2
#   #  print(mid)
#   else:
#    return True
#  return False

# print(passe(nums))


# nums=[0,0,0,1,1,1]
# count=0
# for i in nums:
#   if i==0:
#     count+=1
# print(count)


# class vehicle:
#   def __init__(self,brand):
#     self.brand=brand
#   def start(self):
#     print(f"{self.brand} start")
# class Car(vehicle):
#   def __init__(self, brand,type):
#     self.type=type
#     super().__init__(brand)
#   def fuel(self):
#     print(f"fuel type is {self.type}")

# st=Car("Audi","Diesel")
# st.start()
# st.fuel()

# class person:
#   def __init__(self,name,age):
#       self.name=name
#       self.age=age
#   def introduce(self):
#      print(f"{self.name} and {self.age}")
# class student(person):
#    def __init__(self, name, age,grade):
#       self.grade=grade
#       super().__init__(name, age)
#    def introduce(self):
#       super().introduce()
#       print(f"{self.name} and {self.age} and {self.grade}")

# st=student("taimour",22,"B+")
# st.introduce()
# class Animal:
#   def __init__(self):
#     pass
#   def sound(self):
#     print("Animal make sound")
# class Dog(Animal):
#   def __init__(self):
#     super().__init__()
#   def sound(self):
#     super().sound()
#     print("Bark")
# class Cat(Animal):
#   def __init__(self):
#     super().__init__()
#   def sound(self):
#     print("Meow")

# st=Dog()
# st.sound()

# nt=Cat()
# nt.sound()
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def show(self):
#         print(f"Name: {self.name}, Salary: {self.salary}")


# class Manager(Employee):
#     def __init__(self, name, salary, team_size):
#           # calling parent constructor
#         self.team_size = team_size

#     def show(self):
#         super().show()
#         print(f"Team Size: {self.team_size}")


# # Test
# m = Manager("Taimour", 50000, 5)
# m.show()