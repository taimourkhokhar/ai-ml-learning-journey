"""Iterator"""
# """Iterator that loops forever over the list"""
# dic={
#   "name":"Taimour",
#   "age":23,
#   "city":"Lahore"
# }


# for name,val in dic.items():
#   print(f"key of dictionary is ${name} and value is ${val}")

# 1. Define the simple iterator function
# def get_details(person_dict):
#     yield person_dict.get("name")
#     yield person_dict.get("age")
#     yield person_dict.get("city")

# # 2. Your data
# user = {"name": "Alice", "age": 28, "city": "New York"}

# # 3. Use it in a simple loop
# for detail in get_details(user):
#     print(detail)


#generators code in python

# def count_up_to(n):
#   count = 1
#   while count <= n:
#     yield count
#     count += 1

# for num in count_up_to(5):
#   print(num)


# def large_sequence(n):
#   for i in range(n):
#     yield i

# # this does not create a million numbers in memory

# gen=large_sequence(10000000)
# print(next(gen))
# print(next(gen))
# print(next(gen))


#generator that yields the multiplication of table of a given number

# def table(n):
#   for i in range(1,11):
#      yield i*n


# my_table=table(5)

# print(next(my_table))
# print(next(my_table))
# print(next(my_table))
# print(next(my_table))
