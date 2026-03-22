#Create a class student and name,marks and method to display info

# class student:
#   def __init__(self,name,marks):
#     self.name=name
#     self.marks=marks

#   def displayInfo(self):
#     print("Student name is ",self.name)
#     print("Student age is ",self.marks)


# st=student("Taimour",22)
# st.displayInfo()


#create bankaccount class deposit withdraw and checkbalance


# class BankAccount:
#     def __init__(self, initial_balance=5000):
#         self.balance = initial_balance
   
#     def deposit(self):
#         amount = int(input("Enter amount to add: "))
#         self.balance += amount 
#         print(f"Total balance now is: {self.balance}")

#     def withdraw(self):
#         amount = int(input("How much do you want to withdraw? "))
#         if amount > self.balance:
#             print("Insufficient funds!")
#         else:
#             self.balance -= amount
#             print(f"Your balance now is: {self.balance}")

# bn = BankAccount(5000)
# bn.deposit()  
# bn.withdraw() 



#create a car class method to show brand and speed and method to increase speed 

# class car:
#   def __init__(self,brand,speed):
#     self.brand=brand
#     self.speed=speed

#   def show_detail(self):
#     print("Car brand is ",self.brand)
#     print("Car speed is ",self.speed)
#   def increase_speed(self):
#     print("Car speed increase",self.speed+10)
# cr=car("Audi",300)
# cr.show_detail()
# cr.increase_speed()



# class animal with inheritance

# class Animal:
#   def __init__(self, speak):
#     self.speak = speak

#   def speak_sound(self):
#     print("Animal speaking", self.speak)


# class Dog(Animal):
#   def speak_sound(self):
#     print("Dog speaking", self.speak)


# an = Animal("Woo")
# an.speak_sound()

# dg = Dog("Waooo")
# dg.speak_sound()



#create a person class create student that inherting it and add extra field of marks

# class Person:
#   def __init__(self,name,age):
#     self.name=name
#     self.age=age
#   def info(self):
#     print("Name is ",self.name)
#     print("Age is ",self.age)

# class student(Person):
#   def __init__(self, name, age,marks):
#     super().__init__(name, age)
#     self.marks=marks

#   def info(self):
#     print("Student name is ",self.name)
#     print("Student age is ",self.age)
#     print("Student marks is ",self.marks)


# p=Person("taimour",22)
# p.info()


# st=student("Taimour",22,211)
# st.info()




#Create Vehical class and child classes are car bike add start engine method in both


# class Vehicle:
#   def __init__(self) -> None:
#     pass
#   def start_engine(self):
#     print("Vehicle start engine")


# class Car(Vehicle):
#   def __init__(self) -> None:
#     super().__init__()

#   def start_engine(self):
#     print("This is Car engine")


# class Bike(Vehicle):
#   def __init__(self) -> None:
#     super().__init__()
#   def start_engine(self):
#     print("This is Bike engine")





# vh=Vehicle()
# vh.start_engine()


# cr=Car()
# cr.start_engine()

# bk=Bike()
# bk.start_engine()