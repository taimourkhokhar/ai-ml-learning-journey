# import math

# num = 6
# is_prime = True

# if num <= 1:
#     is_prime = False
# else:
#     # Check only up to the square root
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             is_prime = False
#             break

# if is_prime:
#     print(f"{num} is prime")
# else:
#     print(f"{num} is not prime")

nums=[1,2,3,4,5,6,7,8,9]
is_prime=True
for i in nums:
  if i%2==0:
    is_prime=False
  if i%i==0:
    is_prime=False

if is_prime:
  print("prime numbers are",nums)
else:
  print("Not a prime numbers")