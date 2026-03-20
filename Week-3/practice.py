#1 take a number from user and print
# import math
# user_input=int(input("Enter a number"))

# print("Square  is", user_input*user_input)
# print("Cube is ",user_input*user_input*user_input)
# print("Square root is",math.sqrt(user_input))
#2 take a string then count vowels and consonants
# user_input=input("Enter any word ")
# consonant_count=0
# vowel_count=0
# for i in user_input:
#   if i in 'aeiou':
#     vowel_count+=1
    
#   else:
#     consonant_count+=1
# print("Vowel count in this string is",vowel_count)
# print("consonant count in this string is",consonant_count)
#reverse a string without using slicing 
# print(user_input[::-1])
#check if a number is positive negative or zero
# user_input=int(input("Enter any number " ))
# if user_input>0:
#   print("Input number is positive")
# elif user_input<0:
#   print("Input number is negative")
# else:
#   print("Number is zero")


#take a string print uppercase lowercase title case

# user_input=input("Enter any word ")

# print(user_input.upper())
# print(user_input.lower())
# print(user_input.title())


#1 Given a list and create a new list with squares of each number

# nums=[1,2,3,4,5]

# square=[]

# for i in nums:
#   square.append(i*i)
# print(square)



#2 Remove a duplicates from a list using set

# nums=[1,2,3,2,3,4,5,6]
# new_nums=set(nums)
# print(new_nums)


#3 Create a dictionay and add new key city


# address={
#   "name":"Taimour",
#   "age":20
# }

# address["city"]="Lahore"


# print(address)



#find maximum and minimum value in list


# nums=[1,2,3,4,5]

# max=-1
# min=nums[4]
# for i in nums:
#   if i>max:
#     max=i
# print(max)

# for i in nums:
#  if i<min:
#    min=i
# print(min)




#convert list into tuple and tuple into list

# nums=[1,2,3,4]
# to_tuple=tuple(nums)
# to_list_again=list(to_tuple)
# print(type(to_list_again))


#1 check if a number is even or odd
# nums=[2,3,4,5,6,7,8]
# for i in nums:
#   if i%2==0:
#     print("Number is even")
#   else:
#     print("number is odd")


#print numbers from 1 to 20 but skip multiple of 3

# for i in range(1,21):
#   if i%3==0:
#     continue
#   else:
#     print(i)

#find the sum of all number i na list

# nums=[1,2,3,4,5]

# sum=0

# for i in nums:
#   sum+=i
# print("sum of all numbers in list is ",sum)



#print multiplication table of number

# user_input=int(input("Enter a table number"))


# for i in range(1,11):
#   print(user_input*i)


#1 create a function and return its sum

# def add(a,b):
#   return a+b

# print(add(4,5))


# start=int(input("Enter a starting number"))
# end=int(input("Enter a ending number"))

# def Check_prime(start,end):
#   prime=[]
#   for i in range(start,end+1):
#     if i<2:
#       continue
#     is_prime=True
#     for j in range(2,i):
#       if i%j==0:
#        is_prime=False
#     if is_prime:
#       prime.append(i)
#   print("These are prime number",prime)

# Check_prime(start,end)



#write a function that takes list and return sum and average

# num=[1,2,3,4,5,6]

# def Sum_Avg(nums):
#   average=0
#   sum=0
#   for i in nums:
#     sum+=i
#     average=sum/len(nums)
#   print("Sum of list is ",sum)
#   print("Average of list is",average)



# Sum_Avg(num)


#use lambda to square a number

# user=int(input("Enter any number "))

# ans=lambda x:x*x

# print(ans(user))





# use lambda with map function

# nums=[1,2,3,4]


# ans=list(map(lambda x:x*x,nums))

# print(ans)

