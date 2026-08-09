# Input: s = "IceCreAm"

# Output: "AceCreIm"


# input=list("IceCreAm")
# left=0
# vowel=set("aeiouAEIOU")
# right=len(input)-1
# while left<right:
#   if input[left] not in vowel:
#     left+=1
#   elif input[right] not in vowel:
#     right-=1
#   else:
#     input[left],input[right]=input[right],input[left]
#     left+=1
#     right-=1
#   result="".join(input)
#   print(result)



# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false

# flowerbed = [1, 0, 0, 0, 1]
# n = 1

# count = 0
# length = len(flowerbed)

# for i in range(length):
#     if flowerbed[i] == 0:
#         left_empty = (i == 0) or (flowerbed[i - 1] == 0)
#         print(left_empty)
#         right_empty = (i == length - 1) or (flowerbed[i + 1] == 0)
#         if left_empty and right_empty:
#             flowerbed[i] = 1 
#             count += 1
#     print(i)
# if count >= n:
#     print("true")
# else:
#     print("false")