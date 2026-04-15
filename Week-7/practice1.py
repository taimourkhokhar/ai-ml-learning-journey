# nums=[0,0,0,1,1,1]
# index=0

# for i in range(len(nums)):
#   if nums[i]!=0:
#     print(nums[i])
#     nums[index],nums[i]=nums[i],nums[index]

#     index=index+1
# print(nums)

# import numpy as np

# vl=np.array([[1,2,3,4,5],[5,6,7,8,9]],dtype=int)

# print(vl.ndim)
# print(vl.shape)

# print(vl.size)

nums=[0,1,0,3,12]
index=0

for i in range(len(nums)):
  if nums[i]!=0:# 
    temp=nums[i]
    nums[i]=nums[index]
    nums[index]=temp
    print(nums[i])
    index+=1
print(nums)