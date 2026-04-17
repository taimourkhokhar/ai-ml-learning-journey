# height = [1,8,6,2,5,4,8,3,7]
# def main(ls):
#  max_value=0
#  left=0
#  right=len(height)-1# 9-1 which is 8

#  while left<right:
#   width=right-left # here 9-0 so 8 is width

#   current_height=min(height[left],height[right])

#   current_area=width*current_height
#   max_value=max(max_value,current_area)
#   if height[left]<height[right]:
#     left+=1
#   else:
#     right-=1
#  return max_value

# print(main(height))





# import threading
# import time

# def task(name):
#   for i in range(3):
#     print(name,i)
#     time.sleep(3)

# t1=threading.Thread(target=task,args=("A",))
# t2=threading.Thread(target=task,args=("B",))

# t1.start()
# t2.start()

# t1.join()
# t2.join()
# from multiprocessing import Process
# import time

# def task():
#     for i in range(3):
#         print("Running", i)
#         time.sleep(1)

# if __name__=="__main__":



#  p1 = Process(target=task)
#  p2 = Process(target=task)

#  p1.start()
#  p2.start()

#  p1.join()
#  p2.join()


# Q1

# Create two threads:

# one prints numbers 1 to 5
# second prints letters A to E


# def num(n):
#   for i in n:
#     print(i)
#     time.sleep(3)
# def alpha(s):
#   for i in s:
#     print(i)
#     time.sleep(3)
# n=[1,2,3,4,5]
# s=['a','b','c','d','e']
# t1=threading.Thread(target=num,args=(n,))
# t2=threading.Thread(target=alpha,args=((s,))
# )

# t1.start()
# t2.start()
# t1.join()
# t2.join()
# import threading
# import time

# def filer1(name):
#   for i in range(1,5):
#     print(name,i)
#     time.sleep(3)


# t1=threading.Thread(target=filer1,args=('file 1 downloading',))
# t2=threading.Thread(target=filer1,args=('file 2 downloading',))

# t1.start()
# t2.start()
# t1.join()
# t2.join()

# Q1

# Create 2 processes:

# one prints squares 1 to 5
# second prints cubes 1 to 5

from multiprocessing import Process
import time
def square():
  for i in range(1,6):
    print("square",i*i)
    time.sleep(3)
def cube():
  for i in range(1,6):
    print("cube",i**3)
    time.sleep(3)
if __name__=="__main__":

 t1=Process(target=square)
 t2=Process(target=cube)
 t1.start()
 t2.start()
 t1.join()
 t2.join()