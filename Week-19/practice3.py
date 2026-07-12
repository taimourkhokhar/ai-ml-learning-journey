#create a new list that only containing the square of only even numbers
# numbers=[1,2,3,4,5,6,7,8,9,10]
# even_square=[x*x for x in numbers if x%2==0]
# print(even_square)


#Create a new list containing only name whose length is greater than 4 converted to uppercase

# names=["Ali","Ahmad","Sara","John","Ayesha"]
# new_names=[x.upper() for x in names if len(x)>4]
# print(new_names)


#flatten the matrix into a single list using one list comprehension
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# flat_list=[]

# for row in matrix:
#   for element in row:
#     flat_list.append(element)

# print(flat_list)

# # flat_list=[x for row in matrix for x in row]
# print(flat_list)

# numbers = [1,2,3,4,5]

# square={x:x*x for x in numbers}

# print(square)


# words = ["apple", "banana", "grape", "kiwi"]

# lengther={x:len(x) for x in words}
# print(lengther)


# students = {
#     "Ali":85,
#     "Ahmed":55,
#     "Sara":91,
#     "John":40
# }

# st={x:y for x,y in students.items() if y>=60}
# print(st)


# numbers = [1,2,2,3,4,4,5,6]

# square=(x*x for x in numbers)
# print(square)


# words = ["apple", "banana", "APPLE", "Banana", "grape"]

# lower_set = {x.lower() for x in words}

# print(lower_set)

# sentence="Python Programming"

# st={x for x in sentence if x in "aeiou"}
# print(st)

#Decorators in Python

# def greet_decorator(func):
#   def wrapper():
#     return "Its before greeting"+func()+"its after greeting"
#   return wrapper
# @greet_decorator
# def myfunction():
#   return "Hello sally"
# print(myfunction())