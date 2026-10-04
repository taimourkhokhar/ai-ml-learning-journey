strs = ["flower","flow","flight"]
# Output: "fl"
def longestCommonPrefix(strs):
        if not strs:
            return ""
        
        # Take the first string as a reference baseline
        first_str = strs[0]
        
        for i, char in enumerate(first_str):
            for s in strs[1:]:
                # If index exceeds the string length or characters mismatch
                if i == len(s) or s[i] != char:
                    return first_str[:i]
                    
        return first_str

print(longestCommonPrefix(strs))