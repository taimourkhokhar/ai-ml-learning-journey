
# from scipy import stats
# import numpy as np

# data = [10,12,11,13,12,14,500]

# z_scores = np.abs(stats.zscore(data))

# print(z_scores)


# filtered = []

# for i in range(len(data)):
#     if z_scores[i] < 3:
#         filtered.append(data[i])

# print(filtered)


# nums = [0,1,1,1,0,1,1,0,1]

# left = 0
# zero_count = 0
# max_len = 0

# for right in range(len(nums)):## right is at index 0 also 

#     if nums[right] == 0:# check if nums of right i mean at 0 index it has zero value so it  is tur
#         zero_count += 1## zero count will be one

#     while zero_count > 1: #check zero count greater than 1 or not because we have to maintain at least one zero

#         if nums[left] == 0:# check if nums left=0
#             zero_count -= 1

#         left += 1

#     max_len = max(max_len, right - left)

# print(max_len)

