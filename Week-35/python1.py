# # Input: num1 = "11", num2 = "123"
# # Output: "134"
# num1="11"
# num2="123"
# len1=len(num1)
# len2=len(num2)
# out=0
# for i,j in zip(num1,num2):
#     out+=i
#     out+=j
# print(out)
#wrong approch


num1 = "11"
num2 = "123"

i = len(num1) - 1
j = len(num2) - 1
carry = 0
result = []

while i >= 0 or j >= 0 or carry:
    d1 = int(num1[i]) if i >= 0 else 0
    d2 = int(num2[j]) if j >= 0 else 0

    total = d1 + d2 + carry
    result.append(str(total % 10))
    carry = total // 10

    i -= 1
    j -= 1

print("".join(reversed(result)))  # 134