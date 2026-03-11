def print_all_items(items):
  for item in items: # The loop runs 'n' times
    print(item)
# def get_squared_numbers(numbers):
#   squared_numbers=[]
#   for n in numbers:
#     squared_numbers.append(n*n)
#   return squared_numbers


# numbers=[2,5,8,9]
# get_squared_numbers(numbers)
## O(n) its linear time because if input increase time also increase







numbers=[3,6,4,2,3,6,8,9]

for i in range(len(numbers)):
  for j in range(i+1,len(numbers)):
    if numbers[i]==numbers[j]:
      print(numbers[i])
      break

 
