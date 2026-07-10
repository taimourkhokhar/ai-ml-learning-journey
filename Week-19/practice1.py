#inheritance
# class Person:
#   def __init__(self,name,age):
#     self.name=name
#     self.age=age
#   def display_info(self):
#     pass
  
# class Student(Person):
#   def __init__(self, name, age,grade):
#     self.grade=grade
#     super().__init__(name, age)
#   def display_info(self):
#     print(f"Name: {self.name} Age is {self.age} grade is {self.grade}")    

# st=Student("Taimour",22,"A")
# st.display_info()


# class vehicle:
#   def __init__(self):
#     pass
#   def start_engine(self):
#     pass
#   def stop_engine(self):
#     pass
# class Car(vehicle):
#   def __init__(self):
#     super().__init__()
#   def start_engine(self):
#     print("Car engine start")
#   def stop_engine(self):
#     print("Car engine stop")

# class Bike(vehicle):
#   def __init__(self):
#     super().__init__()
#   def start_engine(self):
#     print("Bike engine start")
#   def stop_engine(self):
#     print("Bike engine stop")
    
# cr=Car()
# cr.start_engine()
# cr.stop_engine()

# bk=Bike()
# bk.start_engine()
# bk.stop_engine()

class employee:
  def __init__(self,name,salary=5000):
    self.name=name
    self.salary=salary
  def calculate_bonus(self):
    pass
  
class Manager(employee):
  def __init__(self, name, salary):
    super().__init__(name, salary)
  def calculate_bonus(self):
    print(f"Name of employee is {self.name} and salary is {self.salary*20}")
    
class Devolper(employee):
  def __init__(self, name, salary=5000):
    super().__init__(name, salary)
  def calculate_bonus(self):
    print(f"Name of employee {self.name} and salary is {self.salary*10}")
    
mn=Manager("Taimour",5000)
dv=Devolper("zaim",5000)

mn.calculate_bonus()
dv.calculate_bonus()