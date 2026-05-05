# nums = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
# k = 2

# nums.sort() 

# left = 0
# right = len(nums) - 1
# count = 0

# while left < right:
#     sums = nums[left] + nums[right]
    
#     if sums == k:
#         count += 1
#         left += 1
#         right -= 1
#     elif sums < k:
#         left += 1
#     else:
#         right -= 1

# print(f"Pairs found: {count}")




nums = [1,12,-5,-6,50,3]
k = 4
windo_sum=sum(nums[:k])#already sum elemetn like 1+12-5-6
max_sum=windo_sum
for i in range(k,len(nums)):# so we start from 4 index  50
  windo_sum=windo_sum-nums[i-k]+nums[i]# we do window_sum
  if windo_sum>max_sum:
    max_sum=windo_sum

print(max_sum)
