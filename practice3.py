# #Program that ask the user to input two numbers and prints
# user_input=int(input("Enter a number 1"))
# user_input1=int(input("Enter a number 2"))

# def add(a,b):
#   return a+b

# def difference(a,b):
#   return a-b

# def product(a,b):
#   return a*b

# def quotient(a,b):
#   try:
#     ans=a/b
#     return ans
#   except ZeroDivisionError:
#     return "YOu cannet divide by zero"
  


# print(add(user_input,user_input1))

# print(difference(user_input,user_input1))

# print(quotient(user_input,user_input1))

# print(product(user_input,user_input1))


#Function that take a string as input and returns


userInput=input("Enter a string")
vowel_count=0
consonants_count=0

def counter(a):
  global vowel_count,consonants_count
  for i in a:
    if i in 'aeiou':
     vowel_count+=1
    else:
      consonants_count+=1


counter(userInput)

print(f"Vowels: {vowel_count}")
print(f"consonant:{consonants_count}")