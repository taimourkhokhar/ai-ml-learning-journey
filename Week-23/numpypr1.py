import numpy as np
# print(np.__version__)
# my_list=[1,2,3,4]
# my_list=my_list*2
# print(my_list)

# array=np.array([1,2,3])
# array=array*2
# print(array)

# print(type(array))

#datatypes in numpy
# array=np.array([1,"banana","orange",True],dtype=np.object_)
# print(array)
# print(array.dtype)
# print(f"{array.nbytes} bytes")


# array=np.array([1,2,3,4,5])
# array=array.astype(np.float16)
# print(array.dtype)

#multidimensiona array
  
  
# array=np.array("A")
# print(array.ndim)
# array1=np.array([[[2,3,4],
#                   [5,6,7],
#                   [4,5,6]]])
# print(array1.ndim)
# print(array1.shape)
# print(array1[0][1][1])
# print(array1[0,0,0])


#reshape funtion that changes shape the array


# array=np.array([1,2,3,4,5,6])

# array=array.reshape(-1,1)

# print(array)
# print(array.shape)

#slicing in numpy

# array=np.array([[1,2,3,4],
#                 [5,6,7,8],
#                 [9,10,11,12],
#                 [13,14,15,16]])

# print(array.ndim)
# print(array.shape)
# # print(array[0:4:2])
# # print(array[::-1])

# # print(array[:,0:3])

# print(array[1:3,1:3])


#numpy arithmetic

#scalar arithmetic

array=np.array([1,2,3])
print(array+1)
print(array **5)

#vectorized math funciton

array=np.array([1,2,3])
print(np.sqrt(array))
print(np.pi)