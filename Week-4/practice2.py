# 1 Variable Numbers Strings

#1 Swap two variable without using a third Variable

# a=5
# b=7
# print("Before swap a anb b are ",a,b)

# a=a+b#now a=5+7 so a=12
# b=a-b # now 12-7 so b=5 change
# a=a-b # now a=12 and b=5 so a is 7 it also change

# print("After swap a and b are",a,b)



#2 take a number and check if it is palindrome 

# num=111
# new=str(num)

# reverse=new[::-1]

# if new!=reverse:
#   print("not palindorme")
# else:
#   print("palindrome")



#3 count vowels and consonants in a string

# user_input="taimour"

# conso_count=0

# vow_count=0

# for i in user_input:
#   if i in 'aeiou':
#     conso_count=conso_count+1
#   else:
#     vow_count=vow_count+1
# print("Vowel count is",vow_count)
# print("Consonant count is ",conso_count)



#4 reverse a string without using slicing ([::-1])

# user="taimour"
# ls=list(user)
# print(ls)
# ls.reverse()
# print(ls)
# result="".join(ls)
# print(result)


#5 find the largest and smallest number in a give input of 3 

# nums=[3,2,3]

# max=nums[0]
# min=nums[-1]

# for i in nums:
#   if i>max:
#     max=i
#   if i<min:
#     min=i
# print("Maximum in this array is ",max)
# print("Minimum number in this array is",min)




#2 lists


# REmove duplicates froma list whtout using sets

# nums=[1,2,2,4]
# same=[]

# for i in nums:#1,2,2,4
#   if i not in same:#check if same presesnt or not if not then add
#     same.append(i)

# print(same)


#Find the second largest in a list


# nums=[1,2,2,3,4]

# max=nums[0]
# sec=nums[0]
# for i in nums:
#   if i>max:
#     max=i
#     for j in nums:
#       if j<max and j>sec:
#         sec=j
# print("Max is ",max)
# print("Second max is ",sec)



#3 merge two list and sort without sorting

# ls1=[1,6,3,4,5]
# ls2=[6,7,8,9]
# ls3=ls1+ls2

# n=len(ls3)
# print(n)

# for i in range(n):
#   for j in range(0,n-i-1):#9-0-1=8 evertime change due to loop 
#     if ls3[j]>ls3[j+1]:
#       temp=ls3[j]
#       ls3[j]=ls3[j+1]
#       ls3[j+1]=temp
# print("Sorted array is ",ls3)


#4 count how many times each element appears(frequency)

nums=[1,2,2,3,4]
count=0

