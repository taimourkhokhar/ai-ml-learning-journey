import numpy as np

# array=np.array([1,2,3,4,5])
# print(type(array))
# print(np.__version__)

# #we can also create tuple for numpy array
# arr = np.array((1, 2, 3, 4, 5))

# print(arr)


#dimension in numpy array
# arr=np.array(42)
# print(arr.ndim)



# a=np.array(42)
# b=np.array([1,2,3,4])
# c=np.array([[1,2,3,4],[5,6,7,8]])
# d=np.array([[[1,2,3],[4,5,6],[7,8,9]]])


# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)


# arr = np.array([1, 2, 3, 4], ndmin=5)

# print(arr)
# print('number of dimensions :', arr.ndim)

#slicing in numpy array

# arr=np.array([1,2,3,4,5,6])
# print(arr[0]+arr[2])

# arr=np.array([[1,2,3,4],[5,6,7,8]])
# print(arr[1,1])
# #now accessing second row 4 column

# print(arr[1,3])


# arr=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
# print(arr[0,1,2])
# print(arr[0,1,1])
# print(arr[0,1,-1])

#slicing in numpy array

# arr=np.array([1,2,3,4,5])
# print(arr[-3:-1])


#numpy data types strings,integer,boolean ,float,complex

# arr=np.array([1,2,3,4,5],dtype='i4')
# print(arr.dtype)
# arr1=np.array(["string"])
# print(arr1.dtype)



# arr=np.array(["apple","banana","cherry"],dtype='i')
# print(arr.dtype)


# arr=np.array([1.1,2.2,3.3,4.4,5.5])

# newArr=arr.astype('i')

# print(arr.dtype)
# print(newArr.dtype)

# arr=np.array([-1,0,3])
# newArr=arr.astype(bool)

# print(newArr)