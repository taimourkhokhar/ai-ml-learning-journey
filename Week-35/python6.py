# # # # Input: nums = [3,0,1]

# # # # Output: 2
# # # numbers=[0,1,2,3,4,5,6,7,8,9]
# # # nums=[3,0,1]
# # # len1=len(nums)
# # # minimums=min(nums)
# # # maximums=max(nums)
# # # for i in range(numbers[minimums],numbers[maximums]+1):
# # #      if i not in nums:
# # #           print(i)

# # class Solution:
# #     def missingNumber(self, nums: list[int]) -> int:
# #         n = len(nums)
        
# #         # Check every number from 0 up to n (inclusive)
# #         for i in range(n + 1):
# #             if i not in nums:
# #                 return i
                
# #         return None

# # Input: nums = [4,1,2,1,2]

# # Output: 4

# nums=[4,1,2,1,2]
# counts={}
# for num in nums:
#     if num in counts:
#         counts[num]+=1
#     else:
#         counts[num]=1
# print(counts)

# for num,count in counts.items():
#     if count==1:
#         print(num)


# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]

# nums1=[1]
# m=1
# nums2=[]
# n=0
# result=[]
# for i in range(0,m):
#     if nums1[i]!=0:
#         result.append(nums1[i])
# print(result)
# for i in range(0,n):
#     if nums2[i]!=0:
#         result.append(nums2[i])
# print(sorted(result))



# Input: digits = [1,2,3]
# Output: [1,2,4]
# Question 1 — Easy: Variables and Numbers

# Create a Python program that:
# - Stores your name, age, and university in variables.

# name="Taimour"
# age=23
# university="uol"
# print(name,age,university)

# sentence = "python is an amazing programming language"
# print(sentence.upper())
# print(sentence.capitalize())
# print(len(sentence))
# new=sentence.replace("python","java")
# print(new)
# print(sentence[13:20])
# print(sentence[::-1])

# numbers=[1,2,3,4,5,6,4,8,9,10]
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
# print(sum(numbers)/len(numbers))
# output=[]
# for i in numbers:
#     if i not in output:
#         output.append(i)
# print(output)
# print(output.sort())

# student = [
#     {"Name": "Taimour", "Age": 23, "Marks": 44},
#     {"Name": "Zaim", "Age": 21, "Marks": 46},
# ]

# highest=student[0]["Marks"]
# for i in student:
#     if i["Marks"]>highest:
#         highest=i["Marks"]
# print(highest)

# student.append({"Name":"joyce","Age":22,"Marks":40})
# print(student)
# student.remove({"Name":"joyce","Age":22,"Marks":40})
# print(student)

list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

list1=set(list1)
list2=set(list2)
print(list1.intersection(list2))
print(list1.difference(list2))
print(list2.difference(list1))
print(list1.union(list2))