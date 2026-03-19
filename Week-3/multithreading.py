import time

import threading


def cal_square(numbers):
  print("Calculate square of numbers")
  for n in numbers:
    time.sleep(0.2)
    print('square',n*n)

def cal_cube(numbers):
  print("Calculate cube of numbers")
  for n in numbers:
    time.sleep(0.2)
    print('cube',n*n*n)

arr=[2,3,8,9]

t=time.time()
# cal_square(arr)
# cal_cube(arr)


t1=threading.Thread(target=cal_square,args=(arr,))

t2=threading.Thread(target=cal_cube,args=(arr,))
t1.start()
t2.start()

t1.join()
t2.join()


print("so ttoal time is",time.time()-t)
