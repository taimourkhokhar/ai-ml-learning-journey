import time

def square():
    start = time.time()
    print(start)
    for i in range(1,1000000000000000000):
        result = i * i
        end = time.time()
        print(end)
        print("time is ", (end - start) * 1000, "ms")
        return result

def cubic():
    start = time.time()
    print(start)
    for i in range(1,1000000000000000000):
      
        result = i * i * i
        end = time.time()
        print(end)
        print("time is ", (end - start) * 1000, "ms")
        return result

ls = [1,2,3,4,5,6,7,8,9,10]

square()
cubic()