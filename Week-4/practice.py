# import time


# def square():
#     start = time.time()
#     print(start)
#     for i in range(1,1000000000000000000):
#         result = i * i
#         end = time.time()
#         print(end)
#         print("time is ", (end - start) * 1000, "ms")
#         return result

# def cubic():
#     start = time.time()
#     print(start)
#     for i in range(1,1000000000000000000):
      
#         result = i * i * i
#         end = time.time()
#         print(end)
#         print("time is ", (end - start) * 1000, "ms")
#         return result

# ls = [1,2,3,4,5,6,7,8,9,10]

# square()
# cubic()


# def my_decorator(func):
#   def wrapper():
#     print("1")
#     func()
#     print("end")
#   return wrapper


# @my_decorator
# def Hello():
#   print("Hello")


# decorated=my_decorator(Hello)
# decorated()

# import time
# ls=[12,12,23,44]
# def my_decorator(func):
#   def wrapper(*args,**kwargs):
#     start=time.time()
#     result=func(*args,**kwargs)
#     end=time.time()
#     duration=(end-start)*1000
#     print(f"Exceted,{func.__name__} in {duration}")
#     return result
#   return wrapper

# @my_decorator
# def square(ls):
#   for i in ls:
#     return i*i
  
# square(ls)

# def functionCounter(func):
#   count=0
#   def wrapper(*args,**kwargs):
#     nonlocal count
#     count+=1
#     res=func(*args,**kwargs)
#     print(f"Called,{func.__name__} {count}")
#     return res
#   return wrapper


    
# @functionCounter
# def hello():
#   print("Hello")


# hello()

# hello()
# hello()
# hello()
# hello()
# hello()