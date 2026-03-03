#takes a number that prints positive even positive odd negative and zero

# user_num=int(input("Enter a number"))

# if user_num>=1 and user_num%2==0:
#   print("number is positive even")
# elif user_num>=1 and user_num%2==1:
#   print("number is positive odd")
# elif user_num<0:
#   print("number is negative")
# else:
#   print("number is zero")


#count vowels and capitalize first letter of each word reverse the string

# text="python is powerful"

# count=0
# for i in text:
#   if i in "aeiou":
#    count+=1
# print("Vowel count",count)

# #for capitalize first letter

# first=text.title()
# print(first)

# #for reverse
# reversed_text = text[::-1]
# print("Reversed:", reversed_text)



#list removes duplicates find largest find second largest without sorting


nums=[4,7,1,9,3,7,4]
unique_nums=[]
for i in nums:
  if i not in unique_nums:
    unique_nums.append(i)

print("After duplicates remove", unique_nums)

#largest in list
max=nums[0]
for i in nums:
  if i>max:
    max=i
print("largest is ",max)

#second largest in list

largest=float('-inf')
second=float('-inf')

for i in nums:
  if i>largest:
    second=largest
    largest=i
  elif i>second and i!=largest:
    second=i

print("largest",largest)
print("second largest",second)


