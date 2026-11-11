# # Input: nums = [0,0,1,1,1,2,2,3,3,4]
# # Output: 5
# #brute force approach
# nums=[1,1,2]
# out=[]
# for i in nums:
#     if i not in out:
#         out.append(i)

# print(len(out))


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        out = []
        for i in nums:
            if i not in out:  # Fixed: check 'out', not 'nums'
                out.append(i)
        
        nums[:] = out
        
        # Return the integer count of unique elements
        return len(nums)