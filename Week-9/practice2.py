import numpy as np

# arr = np.array([1, 2, 3])

# for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
#   print(x)


# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# for x in np.nditer(arr[:, ::2]):
#   print(x)



# arr = np.array([1, 2, 3])

# for idx, x in np.ndenumerate(arr):
#   print(idx, x)


#joining in numpy array
# arr1=np.array([1,2,3,4])
# arr2=np.array([5,6,7,8])
# new=np.concatenate((arr1,arr2))
# print(new)




#for 2-D array

# arr1 = np.array([[[1, 2], [3, 4],[9,10]]])

# arr2 = np.array([[[5, 6], [7, 8],[11,12]]])

# arr = np.concatenate((arr1, arr2), axis=2)

# print(arr)



# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.hstack((arr1, arr2))
# arr=np.vstack((arr1,arr2))
# print(arr)


# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.dstack((arr1, arr2))

# print(arr)



#split array into 3
arr=np.array([1,2,3,4,5,6])
arr1=np.split(arr,3)
print(arr1)