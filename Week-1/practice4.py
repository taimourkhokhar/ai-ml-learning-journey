#function that give square of even numbers

# numbers=[1,2,3,4,5,6,7]


# def square_even(numbers):
#   for i in numbers:
#     if i%2==0:
#       print(i*i)


# square_even(numbers)



#modules in python

import math
import random
#calculate the factorial 


# user=int(input("Enter a number"))

# for i in range(0,user):
#   ans=math.factorial(i)
#   print(ans)



# ans=random.randint(1,10)
# print(ans)



#File handling and exception

# user=input("Enter any quote")
# with open("D://ai engineer//app.txt",'w',encoding='utf-8') as f:
#  f.write(user)


with open("D://ai engineer//app.txt",'r',encoding='utf-8') as O:
 new=O.read()
 print(new)


#check how many vowel in my string
count=0
for i in new:
 if i in 'aeiou':
  count=count+1
print(f"So vowel count {count}")
