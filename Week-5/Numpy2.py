import numpy as np

# arr=np.array([1,2,3,4])
# print(arr.dtype)

# arr1=np.array([1,2,3,5],dtype='S4')

# print(arr1.dtype)


# arr2=np.array(["2","a"],dtype='i')
# # print(arr2)

# copy_arr2=arr2.astype('i')
# print(copy_arr2)

# arr2=np.array([1.2,2.2],dtype='i')
# # print(arr2)

# copy_arr2=arr2.astype('i')
# print(copy_arr2)


# arr3=np.array([1,0,3])
# new_array=arr3.astype(bool)
# print(new_array)
# print(new_array.dtype)

# arr=np.array([1,2,3,4])
# x=arr.copy()
# arr[0]=44

# print(arr)
# print(x)


# arr=np.array([1,2,3,4])
# x=arr.view()
# arr[0]=44

# print(arr)
# print(x)



# arr=np.array([1,2,3,4])

# x=arr.copy()
# y=arr.view()

# print(x.base)
# print(y.base)


#Print the shape of 2-D array

# arr=np.array([[1,2,3,4,5],[4,5,6,7,8]])
# print(arr.shape)
# print(arr.itemsize)
# print(arr.item)


#print the 5-D shape of array
# arr1=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])

# print(arr1.shape)


# arr=np.array([1,2,3,4],ndmin=10)
# print(arr.shape)



#reshape the array like change the dimension 

# arr=np.array([1,2,3,4,5,6,7,8])

# print(arr,arr.ndim)
# new_change=arr.reshape(1,1,8)

# print(new_change,new_change.ndim)


# nums=[0,1,0,3,12]

# zero=[]
# without_zero=[]
# third=[]

# for i in nums:
#   if i == 0:
#     zero.append(i)
#   else:
#     without_zero.append(i)
#   third=without_zero+zero

# print("So final array is",third)

