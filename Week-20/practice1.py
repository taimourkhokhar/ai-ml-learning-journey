word1 = "ab"
word2 = "pqrs"
merge=[]
# count1=len(word1)
# count2=len(word2)
# print(count1,count2)
# count=0
# for i in zip(word1,word2):
#    if len(word1)<len(word2):
#     merge.extend(i)
# final="".join(merge)
# print(final)

# for char1,char2 in zip(word1,word2):
#   merge.append(char1)
#   merge.append(char2)
# remainig=min(len(word1),len(word2))
# remainig=word1[remainig:]+word2[remainig:]
# result="".join(merge)+remainig
# print(result)

# import math
# str1 = "AAAAAB"
# str2 = "AAA"
# common=[]
# def gcd(str1,str2):
#  if str1+str2!=str1+str2:
#      return ""
#  gcd_lenght=math.gcd(len(str1),len(str2))
#  val=str1[:gcd_lenght]
#  if len(val)>=1:
#    return ""
#  if val  in  str2 and str1:
#    return val
#  else:
#    return ""
# print(gcd(str1,str2))



# s = "a good   example"
# nw=[]
# for i in reversed(s.split()):
#    nw.append(i)
# result=" ".join(nw)
# print(result)


#increasing triplet sequence
# nums = [1,2,3,4,5]
# def increase(nums):
#  first=float('inf')
#  second=float('inf')
#  print(first,second)
#  for num in nums:

#    if num<=first:
#       first=num
#       print(first)
#    elif num<=second:
#       second=num
#       print(second)
#    else:
#       return True
#  return False
# print(increase(nums))
# nums = [0,1,0,3,12]
# left=0
# right=0
# while right<=len(nums)-1:
#   if nums[left]==0:
#     nums[left],nums[right]=nums[right],nums[left]
#     right+=1
#   else:
#     left+=1
    
    
# print(nums)

# s = "axc"

# t = "ahbgdc"
# s_ptr=0
# t_ptr=0
# while t_ptr<=len(t)-1:
#   if s[s_ptr]==t[t_ptr]:
#     print("True")
#     t_ptr+=1
#     s_ptr+=1
#   else:
#     t_ptr+=1
#     print("false")


nums = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
k = 2
count=0
left=0
right=len(nums)-1

while left<right:
  if nums[left]+nums[right]==k:
    count+=1
    left+=1
    right-=1
  else:
    left+=1
    right-=1
    
print(count)