# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome
import re

inut="amanaplanacanalpanama"
print(inut[::-1])

s = "A man, a plan, a canal: Panama"

cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

if cleaned_text==cleaned_text[::-1]:
    print(True)
else:
    print(False)

