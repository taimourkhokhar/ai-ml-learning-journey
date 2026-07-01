# class Person:
#   def __init__(self,name,age,graduate=False):
#     self.name=name
#     self.age=age
#     self.graduate=graduate
#   def display_info(self):
#     print("Name of Person is ",self.name)
#     print("Age of person is  ",self.age)
#     print("Graduate is ",self.graduate)

# class Student(Person):
#   def __init__(self, name, age,year, graduate=False):
#     self.year=year
#     super().__init__(name, age, graduate)
#   def display_info(self):
#     print("Name of student is ",self.name)
#     print("Age of student is ",self.age)
#     print("Graduate is ",self.graduate)
#     print("Year is ",self.year)

# class GraduateStudent(Student):
#   def __init__(self, name, age, year,cgpa, graduate=False):
#     self.cgpa=cgpa
#     super().__init__(name, age, year, graduate)
#   def display_info(self):
#     print("Name of student is ",self.name)
#     print("Age of student is ",self.age)
#     print("Graduate is ",self.graduate)
#     print("Year is ",self.year)
#     print("cgpa is ",self.cgpa)


# pr=Person("Taimour",23,False)
# pr.display_info()

# st=Student("Taimour",23,2027,False)
# st.display_info()

# gst=GraduateStudent("taimour",23,2027,3.2,True)
# gst.display_info()


# class payment:
#   def pay(self):
#     print("Payment...... ")

# class creditCard:
#   def pay(self):
#     print("credit card .....")
# class paypal:
#   def pay(self):
#     print("PayPal......")

# class crypto:
#   def pay(self):
#     print("Crypto.....")
# py=payment()
# py.pay()

# cd=creditCard()
# cd.pay()

# pp=paypal()
# pp.pay()

# cr=creditCard()
# cr.pay()

# class Employee:
#   def __init__(self,name,emp_id,base_salary):
#     self.name=name
#     self.emp_id=emp_id
#     self.base_salary=base_salary
#   def calculate_salary(self):
#     return self.base_salary

# class Developer(Employee):
#   def __init__(self, name, emp_id, base_salary,lines_of_code):
#     super().__init__(name, emp_id, base_salary)
#     self.lines_of_code=lines_of_code
#   def calculate_salary(self):
#     return self.base_salary+self.lines_of_code
  
# class Designer(Employee):
#   def __init__(self, name, emp_id, base_salary,number_of_project):
#     super().__init__(name, emp_id, base_salary)
#     self.number_of_project=number_of_project
#   def calculate_salary(self):
#     return self.base_salary*self.number_of_project

# class Manager(Employee):
#   def __init__(self, name, emp_id, base_salary,number_of_team):
#     super().__init__(name, emp_id, base_salary)
#     self.number_of_team=number_of_team
#   def calculate_salary(self):
#     return self.base_salary*self.number_of_team
  

# dev=Developer("Taimour","001",50000,500)

# designer=Designer("Taimour","002",45000,5)

# mgr=Manager("zaim","0002",220000,31)
# team = [dev, designer, mgr]

# # Polling salaries smoothly
# for employee in team:
#     print(f"{employee.name} ({type(employee).__name__}): ${employee.calculate_salary()}")

# from abc import ABC,abstractmethod
# import math

# class shape(ABC):
#   """Abstract base class for all shapes"""
#   @abstractmethod
#   def area(self):
#     """Each shap have its own area method"""

# class Circle(shape):
#   def __init__(self,radius) -> None:
#     super().__init__()
#     self.radius=radius
#   def area(self):
#     return math.pi*(self.radius*self.radius)
  
# class Rectangle(shape):
#   def __init__(self,length,width):
#     self.length=length
#     self.width=width
#   def area(self):
#     return self.length*self.width

# class Triangle(shape):
#   def __init__(self,base,height):
#     self.base=base
#     self.height=height

#   def area(self):
#     return 1/2*self.base*self.height
   

# circle = Circle(radius=5)
# rectangle = Rectangle(length=4, width=6)
# triangle = Triangle(base=3, height=8)

# shapes = [circle, rectangle, triangle]

# for shape in shapes:
#     shape_name = type(shape).__name__
#     print(f"The area of the {shape_name} is: {shape.area():.2f}")


##simple hospital system
from abc import ABC,abstractmethod


class Person(ABC):
  def __init__(self,name,age):
    self.name=name
    self.age=age
  @abstractmethod
  def display_info(self):
     """Abstract method so every class have it own"""
     pass

class Doctor(Person):
  def __init__(self, name, age,specialization,experience):
    super().__init__(name, age)
    self.specialization=specialization
    self.experience=experience
  def display_info(self):
    print(f"Name of Doctor is {self.name} and age of Doctor is {self.age}")
    print(f"Specialization in {self.specialization} and experience is {self.experience}")

class Nurse(Person):
  def __init__(self, name, age,Ward):
    super().__init__(name, age)
    self.Ward=Ward
  def display_info(self):
    print(f"Name of Nurse is {self.name} and age of Nurse is {self.age}")
    print(f"Duty in {self.Ward} Ward")

class Patient(Person):
  def __init__(self, name, age,disease):
    super().__init__(name, age)
    self.disease=disease
  def display_info(self):
    print(f"Name of patient is {self.name} and age of patient is {self.age}")
    print(f"Disease of patient is {self.disease}")

dr=Doctor("Dr.Taimour",23,"Cardiologist","5 years")
nr=Nurse("Zaim",21,"OT")
pt=Patient("Zoin",22,"Skin Infection")

Pr=[dr,nr,pt]

for p in Pr:
    print(f"--- Role: {type(p).__name__} ---")
    
    p.display_info()
    print()  