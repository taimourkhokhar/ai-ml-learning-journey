import numpy as np
#broadcasting in numpy
# array1=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
# array2=np.array([[1],[2],[3],[4]])

# print(array1.shape)
# print(array2.shape)

# print(array1*array2)

# array1=np.array([[1,2,3,4,5,6,7,8,9,10]])
# array2=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

# print(array1.shape)
# print(array2.shape)
# print(array1*array2)

#numpy functions

# array=np.zeros((2,3,10))
# print(array)

# array=np.ones((2,3,10))
# print(array)

# array=np.full((2,3,10),9)
# print(array)

# array=np.eye(2)
# print(array)

# array=np.empty((2,3))
# print(array)


# array=np.arange(0,120,2)
# print(array)



# array1=np.linspace(0,10,4)
# print(array1)


#aggregate functions
# array=np.array([[1,2,3,4,5],[6,7,8,9,10]])

# print(np.sum(array))
# print(np.mean(array))
# print(np.std(array))
# print(np.var(array))
# print(np.min(array))
# print(np.max(array))
# print(np.argmin(array))
# print(np.argmax(array))

#filtering in numpy

# ages=np.array([[21,17,19,20,16,20,18,65],[39,22,15,99,18,19,20,21]])
# teenagers=ages[ages<18]
# adults=ages[ages>=18]
# print(adults)
# print(teenagers)
# adults=np.where(ages>=18,ages,0)
# print(adults)

#random 

# rng=np.random.default_rng(seed=1)

# print(rng.integers(low=1,high=101,size=(3,2)))


# np.random.seed(seed=1)
# print(np.random.uniform(low=-1,high=1,size=3))


# rng=np.random.default_rng()

# # array=np.array([1,2,3,4,5])
# # rng.shuffle(array)
# # print(array)

# fruits=np.array(["apple","orange","banana","coconut","pineapple"])
# fruits=rng.choice(fruits,size=3)
# print(fruits)



#save and load numpy array

# array=np.array([[1,2,4],[4,5,6]])
# np.save("data",array)
# print("Numpy array was saved")


# array1=np.load("./data.npy")
# print(array1)