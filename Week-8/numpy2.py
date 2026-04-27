#copy and view in numpy
import numpy as np

# arr=np.array([1,2,3,4])

# newArr=arr.copy()
# newArr[0]=42

# print(newArr)
# print(arr)

# viewArr=arr.view()
# viewArr[0]=42
# print(viewArr)
# print(arr)


# arr=np.array([1,2,3,4,5,6])

# arr1=arr.copy()
# arr2=arr.view()

# print(arr1.base)
# print(arr2.base)



#shape which give sturcute of array


# arr=np.array([[1,2,3,4],[5,6,7,8]])
# print(arr.shape)


# arr = np.array([1, 2, 3, 4], ndmin=5)

# print(arr)
# print('shape of array :', arr.shape)


#reshaping changing 1d to 2d

# arr=np.array([1,2,3,4,5,6,7,8])
# print(arr.reshape(2,4).ndim)

#reshaping 1d to 3d

# arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])

# print(arr.reshape(2,2,3))


# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# newarr = arr.reshape(3, 3)

# print(newarr)


#check if return array is copy or view

# arr=np.array([1,2,3,4,5,6,7,8])
# print(arr.reshape(2,4).base)


# arr=np.array([1,2,3,4,5,6,7,8])
# print(arr.reshape(2,2,2))


#flaten the array means convert multidimensional array to 1-d array


# arr=np.array([[[1,2,3],[4,5,6],[7,8,9]]])

# print(arr.reshape(-1))


# arr = np.array([[1, 2, 3], [4, 5, 6]])
# newarr = arr.reshape(6)
# print(newarr)