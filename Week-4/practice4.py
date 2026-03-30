# # Q1

# # Create three variables: name, city, profession.
# # Print them in one sentence.


# name="Taimour"
# city="lahore"
# profession="AI Engineer"
# print(f"Name is {name} city is {city} and profession is {profession}")

# # Q2

# # Swap the values of two variables:

# a=5
# b=10
# print("before swap",a,b)
# a=a+b #mow 15
# b=a-b
# a=a-b

# print("After swap",a,b)

# # Q3

# # Create a variable isStudent and assign a boolean value (True/False).
# # Print a message based on it:

# # If true → "You are a student"
# # If false → "You are not a student"

# is_Student=False
# if(is_Student):
#   print("Yes he is a student")
# else:
#   print("No student")


#  2. Numbers (3 Questions)
# Q1
# Take a number and:
# Print its square
# Print its cube

# user=int(input("Enter a number"))
# if user%2==0:
#   print("even")
# else:
#   print("odd")

# Q3

# Take two numbers and:

# Find the maximum
# Find the minimu

# user1=int(input("Enter first number"))
# user2=int(input("Enter second number"))

# if user1>user2:
#   print("Number 1 is maximum and number 2 is minimum")
# else:
#   print("Number 2 is maximum and number 1 is minimum")


# 3. Strings (3 Questions)
# Q1

# Take a string and:

# Print it in uppercase
# Print it in lowercase

# user=input("Enter any word")

# print(user.upper())
# print(user.lower())


# Q2

# Count how many vowels are in a string.

# user=input("Enter any word")

# count=0

# for i in user:
#   if i in 'aeiou':
#     count=count+1

# print("Total vowel in this string is ",count)


# Q3

# Check if a string is a palindrome
# (Reads same forward and backward)

# user=input("Enter any word to check whether it is palindrome")


# user="madam"

# new=list(user)

# new.reverse()

# sentence="".join(new)

# print(sentence)


# if user==sentence:
#   print("True")
# else:
#   print("False")


# IF CONDITION (3 Questions)
# Q1 — Grade System

# Take marks as input and print grade:

# 90+ → A
# 70–89 → B
# 50–69 → C
# Below 50 → Fail

# user=int(input("Enter your marks"))

# if user>=90:
#   print("A")
# elif user>=70 and user <=89:
#   print("B")
# elif user>=50 and user<=69:
#   print("C")
# else:
#   print("fail")


# Q2 — Login System (Real-world 🔥)

# Create two variables:

# username = "admin"
# password = "1234"

# Take input from user:

# If both match → "Login Successful"
# Else → "Invalid Credentials"

# username="admin"
# password="1234"

# user=input("Enter username ")
# pas=input("Enter password ")


# if username==user and password==pas :
#  print("Login Successful")
# else:
#  print("Invalid Credentials")


# Q3 — Number Check (Advanced Logic)

# Take a number and check:

# If divisible by 3 AND 5 → print "FizzBuzz"
# If only divisible by 3 → "Fizz"
# If only divisible by 5 → "Buzz"
# Else → print number


# user=int(input("Enter any number "))

# if user%3==0 and user%5==0:
#   print("fizzbuzz")
# elif user%3==0:
#   print("fizz")
# elif user%5==0:
#   print("Buzz")
# else:
#   print(user)



# Q1 — Print Numbers

# Use a for loop to print numbers from 1 to 10


# for i in range(1,11):
#   print(i)




# Q2 — Sum of Numbers

# Take a number n and print sum from 1 to n

# user=int(input("Enter any number "))
# sum=0
# for i in range(1,user+1):
#   sum+=i
# print(sum)

# Q3 — Count Characters

# Take a string and:

# Count how many letters are in it (ignore spaces)

# 👉 Example:

# Input: "hello world"
# Output: 10

# user=input("Enter any word ")
# new=user.replace(" ","")
# count=0
# for i in new:
#     count=count+1

# print("Final count is ",count)