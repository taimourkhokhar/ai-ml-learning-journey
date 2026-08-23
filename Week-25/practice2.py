# nums=[-5,1,5,0,-7]
# n=len(nums)
# prefix=[0]*n
# prefix[0]=nums[0]
# print(prefix)
# for i in range(1,n):
#   prefix[i]=prefix[i-1]+nums[i]
#   print(max(prefix))

# def pivotIndex(nums):
#     total_sum = sum(nums)
#     left_sum = 0

#     for i, num in enumerate(nums):
#         # Right sum is total_sum - left_sum - num
#         if left_sum == (total_sum - left_sum - num):
#             return i
#         left_sum += num

#     return -1


# nums = [1, 7, 3, 6, 5, 6]
# print(pivotIndex(nums))  # Output: 3


# Example 1:

# Input: arr = [1,2,2,1,1,3]
# Output: true

# arr=[1,2,2,1,1,3]

# occurence={}
# for item in arr:
#   if item in occurence:
#     occurence[item]+=1
#   else:
#     occurence[item]=1
    
# print(occurence)

# same=[]
# for key,val in occurence.items():
#   if val in same:
#     print("false")
#   else:
#     print("false")

# class Solution:

#   def uniqueOccurrences(self, arr: List[int]) -> bool:
#     occurence = {}
#     for item in arr:
#       if item in occurence:
#         occurence[item] += 1
#       else:
#         occurence[item] = 1

#     same = []
#     for key, val in occurence.items():
#       if val in same:
#         return False
#       else:
#         same.append(val)  # Track seen frequencies

#     return True  # Only return True after checking all counts