# def productExceptSelf(nums):
#     n = len(nums)
#     answer = [1] * n
    
   
#     prefix_product = 1
#     for i in range(n):
#         answer[i] = prefix_product
#         prefix_product *= nums[i]
        
   
#     suffix_product = 1
#     for i in range(n - 1, -1, -1):
#         answer[i] *= suffix_product
#         suffix_product *= nums[i]
        
#     return answer

# print(productExceptSelf([1, 2, 3, 4]))


#1-D array
# import numpy as np
# arr=np.array([1,2,3,4])
# print(type(arr))
# print(np.__version__)


#0-D array

import numpy as np

# arr=np.array(42)
# print(np.ndim(arr))
#2-D array
# arr=np.array([[1,2,3,4],[5,6,7,8]])
# print(arr)
# print(np.ndim(arr))


#3-D array

arr=np.array([[[1,2,3,4],[1,2,3,3],[4,5,6,7]]])
print(np.ndim(arr))
print(arr)