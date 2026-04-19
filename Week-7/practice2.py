# nums = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]

# k = 2
# left=0
# right=len(nums)-1
# count=0
# while left<right:
#   current_sum=nums[left]+nums[right]
#   if current_sum==k:
#     count+=1
#     left+=1
#     right-=1
#   elif current_sum<k:
#       left+=1
#   else:
#      right-=1

# print(count)


# nums=[0,0,0,1,1,1]
# left=0
# right=len(nums)-1
# for i in nums:
#   if nums[i]==0:
#      temp=nums[right]
#      nums[right]=nums[left]
#      nums[left]=temp
#   left+=1
#   right-=1
# print(nums)


# 1. Move All Zeros to End

# Given:

# nums = [0,1,0,3,12]

# Move all 0s to the end while keeping order of non-zero elements
# nums = [0, 1, 0, 1, 3, 12]
# left = 0
# right = 0 

# while right < len(nums):# here loop runs right<len 
#     if nums[right] != 0:# if nums[right]!=0 like at index 1 is 1 value so we move in
#         temp = nums[left]# simple swaping
#         nums[left] = nums[right]
#         nums[right] = temp
        
#         left += 1# we move left+=1 so left will be 0 now at 1 index due to swaping
    
#     right += 1# here right will move forward

# print(nums)



# 2. Reverse a List Using Two Pointers

# Given:

# nums = [1,2,3,4,5]

# Reverse it in-place.

# nums=[1,2,3,4,5]

# left=0
# right=len(nums)-1

# while left<right:
#     temp=nums[left]
#     nums[left]=nums[right]
#     nums[right]=temp
#     left+=1
#     right-=1

# print(nums)


# 3. Remove Duplicates from Sorted Array

# Given:

# nums = [1,1,2,2,3,4,4]

# Remove duplicates in-place and return unique part.
# nums = [1,1,2,2,3,4,4]

# left=0
# right=0

# while right<len(nums):
#   if nums[left]==nums[right+1]:
#     del nums[left]
#   left+=1
#   right+=1

# print(nums)