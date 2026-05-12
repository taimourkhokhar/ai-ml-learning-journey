s = "abcabcbb"

char_set = set()
left = 0
max_length = 0

for right in range(len(s)):
    # 1. If we see a duplicate, shrink from the left until it's gone
    while s[right] in char_set:
        char_set.remove(s[left])
        left += 1

    # 2. Add the current character (now guaranteed to be unique in the window)
    char_set.add(s[right])
    
    # 3. Update the max length seen so far
    max_length = max(max_length, right - left + 1)

print(max_length) # Output: 3


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