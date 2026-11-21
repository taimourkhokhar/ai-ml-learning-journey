# for i in range(1,6):
#     for j in range(1,i+1):
#      print("*",end="")
#     print()

# for i in range(1, 6):
#   print("*" * i)

numbers = [10, 15, 20, 25, 30, 35, 40, 45]
even=list(filter(lambda x:x%2==0 , numbers))
square=list(map(lambda x:x**2,numbers))
greater=list(filter(lambda x:x>25,numbers))
result=list(sorted(numbers,key=lambda x:x,reverse=True))
print(result)
print(greater)
print(square)
print(even)