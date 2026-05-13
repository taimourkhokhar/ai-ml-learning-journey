# s = "abcabcbb"

# char_set = set()
# left = 0
# max_length = 0

# for right in range(len(s)):
#     # 1. If we see a duplicate, shrink from the left until it's gone
#     while s[right] in char_set:
#         char_set.remove(s[left])
#         left += 1

#     # 2. Add the current character (now guaranteed to be unique in the window)
#     char_set.add(s[right])
    
#     # 3. Update the max length seen so far
#     max_length = max(max_length, right - left + 1)

# print(max_length) # Output: 3


# import numpy as np

# data = [5,7,8,10,12,15,18,20,100]

# q1=np.percentile(data,25)
# print(q1)
# q3=np.percentile(data,75)
# print(q3)

# iqr=q3-q1

# lowerlimit=q1-1.5*iqr
# upperlimit=q3+1.5*iqr

# for x in data:
#   if x<lowerlimit or x>upperlimit:
#     print("ourtlier is",x)





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



arr = [2,1,5,1,3,2]
k = 3
window=sum(arr[:k])

left=0
maxsum=window
for right in range(k,len(arr)):
  window=window-arr[left]+arr[right]
  left+=1
  if window>maxsum:
    maxsum=window
    
    
print(maxsum)