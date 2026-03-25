# # import threading
# # import time
# # def numbers(ls):

# #   for i in ls:
# #     time.sleep(2)
# #     print( i)
  

# # def letter(nes):
# #   for i in nes:
# #     time.sleep(2)
# #     print(i)
  
# # arr=[1,2,3,4,5]
# # nes=["a","b","c","d","e"]
# # t1=threading.Thread(target=numbers,args=(arr,))
# # t2=threading.Thread(target=letter,args=(nes,))

# # t1.start()
# # t2.start()

# # t1.join()
# # t2.join()

# import threading
# import time

# def thread1():
#  for i in range(1,5):
#    time.sleep(1)
#    print("Thread 1 is running")
 
# def thread2():
#  for i in range(1,5):
#   time.sleep(1)
#   print("Thread 2 is running")
 
# def thread3():
#  for i in range(1,5):
#   time.sleep(1)
#   print("Thread 3 is running")
 

# t1=threading.Thread(target=thread1,args=())
# t2=threading.Thread(target=thread2,args=())
# t3=threading.Thread(target=thread3,args=())

# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()




#multiprocessing

# from multiprocessing import Process
# import time

# def numbers(ls):
#   for i in ls:
#     time.sleep(2)
#     print(i)

# def square(ls):
#   for i in ls:
#     time.sleep(2)
#     print(i*i)


# if __name__=="__main__":  

#  arr=[1,2,3,4,5]

#  p1=Process(target=numbers,args=(arr,))
#  p2=Process(target=square,args=(arr,))
#  p1.start()
#  p2.start()
#  p1.join()
#  p2.join()





# from threading import Thread
# import time

# def numbers(ls):
#   for i in ls:
#     time.sleep(2)
#     print(i)

# def square(ls):
#   for i in ls:
#     time.sleep(2)
#     print(i*i)


# if __name__=="__main__":  

#  arr=[1,2,3,4,5]

#  p1=Thread(target=numbers,args=(arr,))
#  p2=Thread(target=square,args=(arr,))
#  p1.start()
#  p2.start()
#  p1.join()
#  p2.join()



# import threading
# import time

# def task():
#     for _ in range(10**7):
#         pass

# start = time.time()

# t1 = threading.Thread(target=task)
# t2 = threading.Thread(target=task)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# end = time.time()

# print("Threading time:", end - start)





# from multiprocessing import Process
# import time

# def task():
#     for _ in range(10**7):
#         pass

# start = time.time()

# p1 = Process(target=task)
# p2 = Process(target=task)

# p1.start()
# p2.start()

# p1.join()
# p2.join()

# end = time.time()

# print("Multiprocessing time:", end - start)