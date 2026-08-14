# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         max_value=0
#         left=0
#         right=len(height)-1
#         while left<right:
#             width=right-left#so 0-8 which is 8
#             curr_height=min(height[left],height[right])#min is from 1,7 is 1
#             area=curr_height*width# 7*1 which is 7
#             max_value=max(area,max_value)# area is 7 and 1 so 7 is seven
#             if height[left]<height[right]:
#                 left+=1
#             else:
#                 right-=1
#         return max_value



# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.

nums=[1,2,3,4]
k=5
max_value=0
left=0
right=len(nums)-1
while left<right:
  if nums[left]+nums[right]<k:
    left+=1
  elif nums[left]+nums[right]>k:
    right-=1
  else:
    max_value+=1
    left+=1
    right-=1
    
print(max_value)



# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

# nums=[1,12,-5,-6,50,3]
# k=4
# window_sum=sum(nums[:k])
# max_sum=window_sum
# for i in range(k,len(nums)):
#   window_sum=window_sum-nums[i-k]+nums[i]
#   if window_sum>max_sum:
#     max_sum=window_sum
#     print(max_sum)
    
# average=max_sum/k
# print(average)


nums=[1,12,-5,-6,50,3]
k=4

def findMaxAverage(nums,k):
        window_sum=sum(nums[:k])
        max_sum=window_sum
        average=0
        for i in range(k,len(nums)):
            window_sum=window_sum-nums[i-k]+nums[i]
            if window_sum>max_sum:
                max_sum=window_sum
        average=max_sum/k
        return average
          
          
findMaxAverage(nums,k)