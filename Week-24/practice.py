# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# nums=[1,2,3,4]
# result=[]
# for i in range(len(nums)):
#   product=1
#   for j in range(len(nums)):
#     print(j)

#     if i!=j:
#       product*=nums[j]
#   result.append(product)
  
# print(result)

# Input: chars = ["a","a","b","b","c","c","c"]
# Output: 6

from collections import Counter
chars=["a"]
valuecount=Counter(chars)
lister=list(valuecount)
print(len(lister))
value=2*len(lister)
if value%2==1:
  value=value-1
else:
  
 print(value)