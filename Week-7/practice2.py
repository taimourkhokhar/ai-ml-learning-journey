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


nums=[0,0,0,1,1,1]
left=0
right=len(nums)-1
for i in nums:
  if nums[i]==0:
     temp=nums[right]
     nums[right]=nums[left]
     nums[left]=temp
  left+=1
  right-=1
print(nums)