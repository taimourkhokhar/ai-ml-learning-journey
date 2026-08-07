# candies = [2,3,5,1,3]
# extraCandies = 3
# max_c=max(candies)
# boolean=[ num+extraCandies>=max_c for num in candies]
# print(boolean)

# s = "IceCreAm"
# left=0
# right=len(s)-1
# vow='aeiouAEIOU'

# while left<right:
#   if s[left] and s[right] in vow:
#     s[left],s[right]=s[right],s[left]
#     left+=1
#     right-=1
    
# print(s)


# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# nums = [1, 2, 3, 4]

# result = []

# for i in range(len(nums)):
#     product = 1
#     for j in range(len(nums)):
#         if i != j:
#             product *= nums[j]
#     result.append(product)

# print(result)