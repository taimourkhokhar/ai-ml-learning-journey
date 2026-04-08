# word1="abc"
# word2="pqr"

# new=list(word1)
# new.insert(5," ")

# new_str="".join(new)

# print(new_str)

# word1="abc"
# word2="pqr"
# new=""
# len1=len(word1)
# len2=len(word2)
# len3=len1+len2
# print(len3)
# # for m in range(len3):
# for i,j in word1,word2:
#     new+=i+j
# print(new)

# word1 = "abc"
# word2 = "pqr"
# new = ""

# # Since both are length 3, we can loop through the range of the length
# for i in range(len(word1)):
#     new += word1[i] + word2[i]

# print(new) 
# Output: apbqcr
# new=""
# word1="abcd"
# word2="pq"
# for i in range(len(word1)):#i have 3
#   new+=word1[i]+word2[i]
# print(new)


# word1="abcd"
# word2="pq"
# result=""
# max_length=max(len(word1),len(word2))
# #here we choose max lenght to sure htat loop iterate max time may be word1 or word2
# for i in range(max_length):
# #here it run by max 4 due to word1
#   if i<len(word1):#first 1 less than 4 then it add a to the result then move forward
#     result+=word1[i]
#   if i<len(word2):#here same like first 
#     result+=word2[i]
# print(result)  
# 
# Create a variable price = 100. Increase it by 20% and print the new price.
# 

# price=100
# new_price=(20/100)*100
# new_price=new_price+price
# print(new_price) 


#Store a boolean value isLoggedIn. Print different messages based on its value.

# isLoggedIn=False

# if(isLoggedIn):
#   print("You are login")
# else:
#   print("You logout")

#Create a variable and check its data type using Python.

# varia=2
# print(type(varia))


#Find the largest among three numbers.

# num1=22
# num2=24
# num3=20

# if num1>num2 and num1>num3:
#   print("Num1 is maximum")
# elif num2>num1 and  num2>num3:
#   print("Num2 is maximum")
# else:
#   print("Num3 is maximum")



#Convert temperature from Celsius to Fahrenheit.

# celcius=22

# fahrenheit=(celcius*9/5)+32

# print(f"so temperature in farhenheit is {fahrenheit} deg ")


# Take a string and:

# Convert it to uppercase
# Convert it to lowercase

# string="Taimour"
# print(string.upper())
# print(string.lower())


#Count how many vowels are in a string.


# string="taimour"

# count=0
# for i in string:
#   if i in 'aeiou':
#     count+=1
# print("Total vowel in string is ",count)

#Reverse a strign without using reverse


# string="taimour"
# print(string[::-1])

# Check if a string is a palindrome (e.g., "madam").

# string="taimour"
# reverse=string[::-1]
# if string==reverse:
#   print("Palindrome")
# else:
#   print("Not palindrome")

# Check if a string is a palindrome (e.g., "madam").

# string="m adam"

# new=string.replace(" ","")
# print(new)


# word1="abcr"
# word2="pqr"
# result=""
# maxi=max(len(word1),len(word2))
# for i in range(maxi):
#   if i<len(word1):
#     result+=word1[i]
#   if i<len(word2):
#     result+=word2[i]

# print(result)

# candies=[2,3,4,1,3]
# extraCandies=3
# val=[]
# for i in candies:
#   val.append(i+extraCandies)

# min=val[0]

# for i in val:
#   if i<min:
#     val.append("false")
#   else:
#     val.append("false")

# # print(val)
# candies=[2,3,5,1,3]
# extraCandies=3
# result=[]
# maxi=max(candies)

# for i in candies:
#   if i+extraCandies >= maxi:
#     result.append(True)
#   else:
#     result.append(False)
# print(result)

#Create a list of 5 numbers and print the sum of all elements.

# nums=[1,2,3,4,5]
# sum=0

# for i in nums:
#   sum+=i
# print(sum)

# Find the maximum and minimum value in a list.

# nums=[1,2,3,4,5]

# max=nums[0]
# min=nums[0]

# for i in nums:
#   if i>max:
#     max=i
#   if i<min:
#     min=i
# print(f"max and min is",min,max)



# Remove duplicates from a list.

# nums=[2,2,2,1,2,3,4,]
# without_duplicates=[]

# for i in nums:
#   if i not in without_duplicates:
#     without_duplicates.append(i)

# print(without_duplicates)

# def reverseVowels(s):
#     s_list = list(s)
#     vowels_in_s = []
#     for char in s_list:
#         if char in 'aeiouAEIOU':
#             vowels_in_s.append(char)
#     vowels_in_s.reverse()
#     vowel_index = 0
#     for i in range(len(s_list)):
#         if s_list[i] in 'aeiouAEIOU':
#             s_list[i] = vowels_in_s[vowel_index]
#             vowel_index += 1
            
#     return "".join(s_list)

#take alist of numbers and create new with only even numbers

# nums=[1,2,3,4,5,6]

# even=[]

# for i in nums:
#   if i%2==0:
#     even.append(i)

# print(even)