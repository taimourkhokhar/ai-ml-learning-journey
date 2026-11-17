# # Input: nums = [3,0,1]

# # Output: 2
# numbers=[0,1,2,3,4,5,6,7,8,9]
# nums=[3,0,1]
# len1=len(nums)
# minimums=min(nums)
# maximums=max(nums)
# for i in range(numbers[minimums],numbers[maximums]+1):
#      if i not in nums:
#           print(i)

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Check every number from 0 up to n (inclusive)
        for i in range(n + 1):
            if i not in nums:
                return i
                
        return None