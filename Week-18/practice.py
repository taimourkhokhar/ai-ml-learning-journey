# class Student:
#   def __init__(self,name,age):
#     self.name=name
#     self.age=age
#   def info(self):
#     print("Name of student is  ",self.name)
#     print("Age of student is ",self.age)

# student=Student("Taimour",23)
# student.info()

# class rectangle:
#   def __init__(self,length,width):
#     self.length=length
#     self.width=width
#   def area(self):
#     print("The area of rectangle is ",self.length*self.width)

# ar=rectangle(12,12)

# ar.area()

# class BankAccount:
#   def __init__(self,balance):
#     self.balance=balance
    
#   def deposit(self,deposit):
#     self.balance+=deposit
#     print("So current balance after deposit is ",self.balance)
#   def withdraw(self,withdraw):
#     self.balance-=withdraw
#     print("So the current balance after withdraw is ",self.balance)
# ba=BankAccount(5000)
# ba.withdraw(2000)

# class Employee:
#   def __init__(self,name,salary):
#     self.name=name
#     self.salary=salary
#   def increase_salary(self,percent):
#     update=(self.salary/100)*percent
#     print("so the salary after increment is ",self.salary+update)

# emp=Employee("Taimour",50000)
# emp.increase_salary(10)

class Book:
  def __init__(self,title,author,available=True):
    self.title=title
    self.author=author
    self.available=available

  def borrow_book(self):
   if self.available:
     self.available=False
     print(f"Sucessfully you borrow book {self.title}")
   else:
     print(f"{self.title} book is not available")

  def return_book(self):
    if not self.available:
      self.available=True
      print(f"Thank you for returning this book {self.title}")
    else:
      print("This book is already in library")
  def display(self):
        status = "Available" if self.available else "Borrowed/Unavailable"
        print("--- Book Details ---")
        print(f"Title:  {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")
        print("--------------------")
   
bk = Book("Harry Potter and the Prisoner of Azkaban", "J.K. Rowling", True)

# 2. Display initial status
bk.display()

# 3. Try to borrow it
bk.borrow_book()

# 4. Try to borrow it again (should say unavailable now)
bk.borrow_book()

# 5. Display status to see it changed to False/Unavailable
bk.display()

# 6. Return the book
bk.return_book()

# 7. Display final status to see it's available again
bk.display()