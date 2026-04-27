# text="python is great and python is easy"
# dic={}
# for i in text.split():
#   if i not in dic:
#     dic[i]=1
#   else:
#     dic[i]+=1

# print(dic)


#sliding window

# nums = [2,1,5,1,3,2]
# k = 3

# window_sum = sum(nums[:k])   # first 3 elements
# max_sum = window_sum

# print("First window:", nums[:k], "=", window_sum)

# for i in range(k, len(nums)):
#     window_sum = window_sum - nums[i-k] + nums[i]
    
#     print("New window sum:", window_sum)

#     if window_sum > max_sum:
#         max_sum = window_sum

# print("Maximum sum:", max_sum/k)


