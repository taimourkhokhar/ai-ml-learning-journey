# #reverse array without reverse
# # nums=[1,2,3,4,5]
# # left=0
# # right=len(nums)-1

# # while left<right:
# #   nums[left],nums[right]=nums[right],nums[left]
# #   left+=1
# #   right-=1

# # print(nums)

# #how many nums are repeated in array
# # nums=[1,2,3,2,4,5]
# # repeat=[]

# # for i in nums:
# #   if i not in repeat:
# #     repeat.append(i)
# #   else:
# #     print(i)


# #tow pointer moves zero to end

# nums=[0,0,0,1,1,1]

# left=0
# right=len(nums)-1

# while left<right:
#   if nums[left]==0:
#     nums[left],nums[right]=nums[right],nums[left]
#     left+=1
#     right-=1

# print(nums)

numbers = [2,7,11,15]
target = 9
left=0
right=len(numbers)-1
sum=0
arr=[]
while left<right:
  sum=numbers[left]+numbers[right]
  if sum==target:
    arr.append(left+1)
    arr.append(right+1)
  elif sum>target:
    right-=1
  else:
    left+=1


  