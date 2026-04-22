import math

num = 6
is_prime = True

if num <= 1:
    is_prime = False
else:
    # Check only up to the square root
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")