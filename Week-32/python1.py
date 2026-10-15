# # Input: s = "A man, a plan, a canal: Panama"
# # Output: true
# # Explanation: "amanaplanacanalpanama" is a palindrome
# import re

# inut="amanaplanacanalpanama"
# print(inut[::-1])

# s = "A man, a plan, a canal: Panama"

# cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

# if cleaned_text==cleaned_text[::-1]:
#     print(True)
# else:
#     print(False)

# # I=1
# # V=5
# # X=10
# # L=50
# # C=100
# # D=500
# # M=1000
# # output={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
# # s = "LVIII"
# # out=0
# # for i in s:
# #     if i in output:
# #         out+=output[i]
# # print(out)

# # class Solution:

# #     def romanToInt(self, s: str) -> int:
# #         output = {
# #             "I": 1,
# #             "V": 5,
# #             "X": 10,
# #             "L": 50,
# #             "C": 100,
# #             "D": 500,
# #             "M": 1000,
# #         }
# #         out = 0

# #         for i in range(len(s)):
# #             # If a smaller value comes before a larger value, subtract it
# #             if i + 1 < len(s) and output[s[i]] < output[s[i + 1]]:
# #                 out -= output[s[i]]
# #             else:
# #                 out += output[s[i]]

# #         return out

# I=1
# V=5
# X=10
# L=50
# C=100
# D=500
# M=1000
# output={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
# s = "IV"
# out=0
# for i in range(len(s)):
#     if i+1<len(s) and output[s[i]] < output[s[i+1]]:
#         out-=output[s[i]]
#     else:
#         out+=output[s[i]]

# print(out)