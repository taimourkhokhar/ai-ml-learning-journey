# Input: prices = [7,1,5,3,6,4]
# Output: 5

prices=[1,4,2]


left=0
right=len(prices)-1
max_price=0
while right>left:
    diff=prices[right]-prices[left]
    if diff>max_price:
        max_price=diff
    left+=1
    right-=1
print(max_price)
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = max_sum = nums[0]
        
        for num in nums[1:]:
            # Either extend the existing subarray or start fresh at the current element
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
            
        return max_sum