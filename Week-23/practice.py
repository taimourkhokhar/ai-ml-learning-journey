# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"

# word1="ab"
# word2="pqrs"
# com=[]
# for i,j in zip(word1,word2):
#   com.append(i)
#   com.append(j)
#   rem=min(len(word1),len(word2))
#   rem=word1[rem:]+word2[rem:]
#   result="".join(com)+rem
#   print(result)


# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
# Input: str1 = "AAAAAB", str2 = "AAA"
# Output: ""


# import math
# str1="ABCABC"
# str2="ABC"

# def gcd(str1,str2):
#   if str1+str2!=str2+str1:
#     return ""
#   gcd_length=math.gcd(len(str1),len(str2))
#   print(gcd_length)
#   return str1[:gcd_length]
# print(gcd(str1,str2))