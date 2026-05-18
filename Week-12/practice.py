arr = [3, 1, 6, 2, 8, 4]

prefix = [0] * len(arr)
print(prefix)

prefix[0] = arr[0]
print(prefix)

for i in range(1, len(arr)):
    prefix[i] = prefix[i - 1] + arr[i]

    print(prefix)