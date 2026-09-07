#stack practice
# stack=[]
# stack.append("A")
# stack.append("B")
# stack.append("C")
# print("Stack after pushes:",stack)

# if stack:
#   print("Top element (peek):" ,stack[-1])
  
# print("popped:", stack.pop())
# print("popped",stack.pop())
# print("Remaining stack:",stack)


# class Solution:

#   def isValid(self, s: str) -> bool:
#     stack = []
#     # Map closing brackets to their corresponding opening brackets
#     mapping = {")": "(", "}": "{", "]": "["}

#     for char in s:
#       if char in mapping:
#         # Pop the top element if stack is not empty, otherwise set a dummy value
#         top_element = stack.pop() if stack else "#"

#         # Check if the popped bracket matches the expected opening bracket
#         if mapping[char] != top_element:
#           return False
#       else:
#         # Push opening brackets onto the stack
#         stack.append(char)

#     # If the stack is empty, all brackets were validly matched
#     return not stack

# n=1
# while n<=10:
#   print(n)
#   n+=1
  
  
# arr=[2,4,6,8,10]
# sum=0
# i=0
# while i<len(arr):
#   sum+=arr[i]
#   i+=1

# print(sum)

# arr = [3, 8, 11, 14, 20, 7, 6]
# even_count=0
# i=0
# while i<len(arr):
#   if arr[i]%2==0:
#     even_count+=1
#   i+=1
  
# print(even_count)