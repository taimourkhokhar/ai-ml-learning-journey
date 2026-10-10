
# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
nums=[0,1,2,4,5,7]
def summaryRanges(nums):
        result = []#empty
        i = 0
        n = len(nums)# 6 
        
        while i < n:#0<6 its true then while loop run
            start = nums[i]# now start=0
            
            # Move i forward while consecutive elements differ by 1
            while i + 1 < n and nums[i + 1] == nums[i] + 1:# 0+1 < 6 its true and 1 == nums[i] which is 0 its true
                i += 1
            
            # Format range
            if start == nums[i]:
                result.append(str(start))
            else:
                result.append(f"{start}->{nums[i]}")
            
            i += 1
            
        return result



