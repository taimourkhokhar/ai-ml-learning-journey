# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# s = "A man, a plan, a canal: Panama"
# new=s.maketrans('', '', ',;:')
# ch=s.translate(new).replace(" ","").lower()
# print(ch)
# if ch==ch[::-1]:
#   print("Palindrome")
# else:
#   print("not")