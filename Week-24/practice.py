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

# from collections import Counter
# chars=["a"]
# valuecount=Counter(chars)
# lister=list(valuecount)
# print(len(lister))
# value=2*len(lister)
# if value%2==1:
#   value=value-1
# else:
  
#  print(value)


# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# nums=[0,1,0,3,12]
# left=0
# right=1

# while right<len(nums):
#   if nums[right]!=0:
#     nums[left],nums[right]=nums[right],nums[left]
#     left+=1
#   right+=1
  
# print(nums)
    
#     Input: s = "abc", t = "ahbgdc"
# Output: true

# s="abc"
# t="ahbgdc"
# leftptr=0
# rightptr=0
# while rightptr<=len(t)-1:
#   if s[leftptr]==t[rightptr]:
#     leftptr+=1
#     rightptr+=1
#     return True
#   else:
#     rightptr+=1
#     return False