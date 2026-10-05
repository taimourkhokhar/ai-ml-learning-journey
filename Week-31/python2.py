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


class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        result = []
        i = 0
        n = len(nums)
        
        while i < n:
            start = nums[i]
            
            # Move i forward while consecutive elements differ by 1
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1
            
            # Format range
            if start == nums[i]:
                result.append(str(start))
            else:
                result.append(f"{start}->{nums[i]}")
            
            i += 1
            
        return result