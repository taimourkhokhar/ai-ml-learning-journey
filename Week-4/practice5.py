from itertools import batched

nums=[2,1,4,5,4,3]

chunk_size=3

iterator=batched(nums,chunk_size)
chunks=list(iterator)
print(chunks)