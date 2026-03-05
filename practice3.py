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


# userInput=input("Enter a string")
# vowel_count=0
# consonants_count=0

# def counter(a):
#   global vowel_count,consonants_count
#   for i in a:
#     if i in 'aeiou':
#      vowel_count+=1
#     else:
#       consonants_count+=1


# counter(userInput)

# print(f"Vowels: {vowel_count}")
# print(f"consonant:{consonants_count}")


# new = []

# for i in range(1, 11):
#     user = int(input(f"Enter number {i}: "))
#     new.append(user)

# max_val = new[0]
# min_val = new[0]
# evens = []

# for i in new:
#     if i > max_val:
#         max_val = i
    
#     if i < min_val:
#         min_val = i
    
#     if i % 2 == 0:
#         evens.append(i)

# print("-" * 20)
# print(f"Even numbers found: {evens}")
# print(f"The largest number is: {max_val}")
# print(f"The smallest number is: {min_val}")



#create a dictionay for a student with keys: name,rollno,marks (marks should be a list of 5 subjents)
# student_data = {
#   "name": "Taimour",
#   "roll_no": 70147,
#   "marks": {
#     "physics": 77,
#     "math": 88,
#     "chemistry": 32,
#     "biology": 54
#   }
# }

# total = 0
# average=0
# for subject, score in student_data["marks"].items():
#     print(f"{subject}: {score}")
#     total += score
#     average=total/4
#     if average>60:
#         print(f"Student name: {student_data['name']}")
# print(f"Average Marks: {average}")
# print(f"Total Marks: {total}")



#program that two sets of number from user

# set1={1,2,3,4,5,6}
# set2={4,5,6,7,8,9,10}

# ans_set3=set1.union(set2)

# ans_set4=set1.intersection(set2)

# ans_set5=set1.difference(set2)

# print(ans_set5)
# print(ans_set4)
# print(ans_set3)



