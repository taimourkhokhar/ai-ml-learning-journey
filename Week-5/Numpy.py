# import numpy as np
# import sys

# n = 1000

# python_list = list(range(n))
# total_list_size = sys.getsizeof(python_list) + sum(sys.getsizeof(i) for i in python_list)

# arr = np.arange(n)
# total_numpy_size = arr.nbytes # Highly optimized, no pointers needed

# print(f"Total List Memory: {total_list_size} bytes")
# print(f"Total NumPy Memory: {total_numpy_size} bytes")
# print(f"NumPy is {round(total_list_size / total_numpy_size, 1)}x more efficient!")

# l1=[1,2,3,4]
# l2=[4,5,6,7]
# new=tuple(zip(l1,l2))
# print(new)

import time
import numpy as np
# SIZE=1000000

# l1=list(range(SIZE))
# l2=list(range(SIZE))
# start=time.time()
# l3=[x+y for x,y in zip(l1,l2)]
# end=time.time()
# print((end-start))


#performance of numpy

# n1=np.arange(SIZE)
# n2=np.arange(SIZE)
# start=time.time()
# n3=n1+n2
# end=time.time()
# print(end-start)

rev_q1=np.array([[10,12,9],[15,11,13]])

# print(rev_q1[1,2])
# print(rev_q1.itemsize)
# print(rev_q1.shape)

rev_q1.sort()
print(rev_q1)
val=np.zeros((2,3))
print(val)
ans=np.arange(20,30,2)
print(ans)
answer=np.linspace(10,20,20)
print(answer)
minimums=rev_q1.max()
print(minimums)
#for sum

sumer=rev_q1.sum(axis=1)
print(sumer)