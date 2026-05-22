# nums = [1,1,1]
# k = 2
# sum_counts = {0: 1}
# current_sum = 0
# total_subarrays = 0

# for num in nums:
#   current_sum+=num
  
#   difference=current_sum-k
#   if difference in sum_counts:
#     total_subarrays += sum_counts[difference]
#     if current_sum in sum_counts:
#             sum_counts[current_sum] += 1
#     else:
#          sum_counts[current_sum] = 1
            
# print(total_subarrays)


# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         sum_counts = {0: 1}
    
#         current_sum = 0
#         total_subarrays = 0
    
#         for num in nums:
#         # 1. Update the running prefix sum
#           current_sum += num
        
#         # 2. Check if (current_sum - k) exists in our history
#           difference = current_sum - k
#           if difference in sum_counts:
#             # If it exists, add the number of times we've seen it to our total
#             total_subarrays += sum_counts[difference]
            
#         # 3. Record the current_sum in our dictionary so future loops can see it
#           if current_sum in sum_counts:
#             sum_counts[current_sum] += 1
#           else:
#             sum_counts[current_sum] = 1
            
#         return total_subarrays