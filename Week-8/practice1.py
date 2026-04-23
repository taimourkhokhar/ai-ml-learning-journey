# import math

# num = 6
# is_prime = True

# if num <= 1:
#     is_prime = False
# else:
#     # Check only up to the square root
#     for i in range(2,num):
#         if num % i == 0:
#             is_prime = False
#             break

# if is_prime:
#     print(f"{num} is prime")
# else:
#     print(f"{num} is not prime")

nums=[1,2,3,4,5,6,7,8,9]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new = []

for i in nums:
    if i <= 1:
        continue  # Skip 1 because it's not prime
    
    is_prime = True  # Assume it's prime until proven otherwise
    
    # Test divisors from 2 up to the number itself
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break  # Found a divisor, stop checking this number
            
    if is_prime:
        new.append(i)

print(new)  # Output: [2, 3, 5, 7]