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
nums = [1,2,3,4,5]
def increase(nums):
 first=float('inf')
 second=float('inf')
 print(first,second)
 for num in nums:

   if num<=first:
      first=num
      print(first)
   elif num<=second:
      second=num
      print(second)
   else:
      return True
 return False
print(increase(nums))