# nums =[-100000,-100000]
# new=[]
# for i in nums:
#     if i<0:
#         nm=-1*i
#         new.append(nm)
#     else:
#         new.append(i)

# print(new)

# minimum=min(new)
# print("Minimum value in the new list is:", minimum)

# def my_generator():
#   yield 1
#   yield 2
#   yield 3

# for value in my_generator():
#   print(value)

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

# # This doesn't create a million numbers in memory
# gen = large_sequence(1000000)
# print(next(gen))
# print(next(gen))
# print(next(gen))

# def simple_gen():
#   yield "Emil"
#   yield "Tobias"
#   yield "Linus"

# gen = simple_gen()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen )