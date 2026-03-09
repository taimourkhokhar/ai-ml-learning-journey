# def calculate_area(base,height,shape):
#  if shape=='rectangle':
#   return base*height
#  elif shape=='triangle':
#   return 1/2*base*height
#  else:
#   return "Your input is wrong"

# print(calculate_area(4,5,'square'))

# country_info={
#   "China":143,
#   "India":136,
#   "USA":32,
#   "Pakistan":21
# }

# user=input("Enter any query")

# if user=='print':
#   for i,value in country_info.items():
#     print(i,"==>",value)
# elif user=='add':
#   country=input("Enter a country name")
#   if country in country_info:
#     print("country already existed")
#   else:
#     population=int(input("Enter population"))
#     country_info[country]=population
#     for i,value in country_info.items():
#       print(i,"==>",value)
# elif user=='remove':
#   delete=input("Which country delete")
#   if delete in country_info:
#    del country_info[delete]
#    for i,value in country_info.items():
#      print(i,"==>",value)
#   else:
#     print("Country is not presents")


# stock={
#   "info":[600,630,620],
#   "ril":[1430,1490,1567],
#   "mtl":[234,180,160]
# }

# user=input("Enter a query")

# if user=='print':
#   for i,value in stock.items():
#     count=0
#     for j in value:
#       count+=j
#     print(i,"==>",value,"==>",count/3)
# elif user=="add":
#   ticker=input("Enter name of stock")
#   price=int(input("Enter a price of stock"))

#   if ticker in stock:
#     for k,val in stock.items():
#       counter=0
#       for l in val:
#         counter+=l
#       val.append(price)
#       print(k,"==>",val,"==>",counter/4)




# try:
#   user=int(input("Enter a number"))
#   result=10/user
# except ValueError:
#   print("Enter a valid number")
# except ZeroDivisionError:
#   print("You cannot divide by zero")
# else:
#   print(f"Result is {result}")
# finally:
#   print("Execution complete")

class employee:
  def __init__(self,id,name):
    self.id=id
    self.name=name

  def display(self):
   print(self.id,self.name)



emp=employee(1,"coder")
emp.display()


del emp.id
# Deleting the object itself
try:
    print(emp.id)
except NameError:
    print("emp.id is not defined")

del emp
try:
    emp.display()  # it will gives error after deleting emp
except NameError:
    print("emp is not defined")
