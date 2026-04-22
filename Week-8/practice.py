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


# s = "Hello World "
# new=s.split()
# print(len(new[-1]))

class Solution:
    def romanToInt(self, s: str) -> int:
        # Map each Roman numeral to its integer value
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i+1]]:
                total -= roman_map[s[i]]
            else:
                total += roman_map[s[i]]
                
        return total