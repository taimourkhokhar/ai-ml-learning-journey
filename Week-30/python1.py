# I=1
# V=5
# X=10
# L=50
# C=100
# D=500
# M=1000
# output={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
# s = "LVIII"
# out=0
# for i in s:
#     if i in output:
#         out+=output[i]
# print(out)

# class Solution:

#     def romanToInt(self, s: str) -> int:
#         output = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000,
#         }
#         out = 0

#         for i in range(len(s)):
#             # If a smaller value comes before a larger value, subtract it
#             if i + 1 < len(s) and output[s[i]] < output[s[i + 1]]:
#                 out -= output[s[i]]
#             else:
#                 out += output[s[i]]

#         return out

I=1
V=5
X=10
L=50
C=100
D=500
M=1000
output={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
s = "IV"
out=0
for i in range(len(s)):
    if i+1<len(s) and output[s[i]] < output[s[i+1]]:
        out-=output[s[i]]
    else:
        out+=output[s[i]]

print(out)