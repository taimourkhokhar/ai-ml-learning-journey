# 4. Two Sum (Sorted Array)
# nums = [1,2,3,4,6]
# target = 6

# Find two numbers whose sum = target.

# nums = [1,2,3,4,6]
# target = 5

# left=0
# right=1


# while right<len(nums):
#   if nums[left]+nums[right]==target:
#     print(nums[left],"and",nums[right])
#   left+=1
#   right+=1


# 1. Check Palindrome
# word = "madam"

# Return True if palindrome.

# word="madam"
# def check_pal(word):
#  if word==word[::-1]:
#   return True
#  else:
#   return False
 
# print(check_pal(word))

# height = [1,8,6,2,5,4,8,3,7]
# left=0
# right=len(height)-1
# maxe=0

# while left<right:
#   width=right-left
#   max_area=width*min(height[left],height[right])
#   if max_area>maxe:
#    maxe=max_area
#   if height[left]<height[right]:
#     left+=1
#   else:
#     right-=1
# print(maxe)


# nums = [2,0,2,1,1,0]
# left=0
# i=0
# right=len(nums)-1
# while i<=right:
#   if nums[i]==0:
#     temp=nums[left]
#     nums[left]=nums[i]
#     nums[i]=temp
#     left+=1
#     i+=1
#   elif nums[i]==2:
#     temp=nums[right]
#     nums[right]=nums[i]
#     nums[i]=temp
#     right-=1
#   else:
#     i+=1

# print(nums)




# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3


# nums=[1]
# counts = {}
# threshold = len(nums) / 2
# print(threshold)
# for i in nums:
#   counts[i] = counts.get(i, 0) + 1
            
#   if counts[i] > threshold:
#          print( i)



# st="taaatmi"

# dic={}

# for i in st:
#   if i not in dic:
#     dic[i]=1
#   else:
#     dic[i]+=1

# print(dic)


# st=["python","python","java","javascript"]

# dic={}
# for i in st:
#   if i not in dic:
#     dic[i]=1
#   else:
#     dic[i]+=1

# print(dic)

#do like if st has python move it to end 

# st=["python","python","java","javascript"]
# left=0
# right=len(st)-1

# while left<right:
#   if st[left]!="python":
#     left+=1
#   elif st[right]=="python":
#     right-=1
#   else:
#     st[left],st[right]=st[right],st[left]
#     left+=1
#     right-=1
# print(st)

 
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


nums = [0,2,1,0,1,2,1]

left = 0
now = 0
right = len(nums) - 1

while now <= right:

    if nums[now] == 0:
        nums[left], nums[now] = nums[now], nums[left]
        left += 1
        now += 1

    elif nums[now] == 1:
        now += 1

    else:   # nums[now] == 2
        nums[now], nums[right] = nums[right], nums[now]
        right -= 1

    print(nums)

print("Final:", nums)