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