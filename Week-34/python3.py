# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# new_list=[x for x in fruits if "a" in x]
# print(new_list)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# square=[x*x for x in numbers]
# print(square)

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# flat_list = [item for sublist in matrix for item in sublist]
# print(flat_list)

# def changecase(func):
#   def myinner():
#     print("Function is starting")
#     return func()+ "Function is ending"
#   return myinner

# @changecase
# def hello():
#   return "Hello Taimour"

# print(hello())

# import time

# def timer(func):
#     def inner():
#         start_time = time.time()     
#         result = func()              
#         end_time = time.time()        
        
#         elapsed = end_time - start_time 
#         print(f"Time taken: {elapsed:.6f} seconds")
        
#         return result                  
#     return inner

# @timer
# def iterations():
#     for i in range(1, 100000):
#         i

# iterations()  