# # # Input: num1 = "11", num2 = "123"
# # # Output: "134"
# # num1="11"
# # num2="123"
# # len1=len(num1)
# # len2=len(num2)
# # out=0
# # for i,j in zip(num1,num2):
# #     out+=i
# #     out+=j
# # print(out)
# #wrong approch


# num1 = "11"
# num2 = "123"

# i = len(num1) - 1# here i is 1
# j = len(num2) - 1# here is j is 2
# carry = 0
# result = []

# while i >= 0 or j >= 0 or carry:
#     d1 = int(num1[i]) if i >= 0 else 0
#     d2 = int(num2[j]) if j >= 0 else 0

#     total = d1 + d2 + carry
#     result.append(str(total % 10))
#     carry = total // 10

#     i -= 1
#     j -= 1

# print("".join(reversed(result)))  # 134

# is_logged_in=False
# def check(func):
#     def wrapper(*args,**kwargs):
#         if is_logged_in:
#             return func(*args,**kwargs)
#         else:
#             print("Acess denied!")
#     return wrapper
# @check
# def view():
#     print("Welcome to dashboard")

# view()
# is_logged_in=True
# view()

import threading
import time
def task1():
    for i in range(1,6):
        print(i)
        time.sleep(0.1)
def task2():
    for letter in ['a','b','c','d','e']:
        print(letter)
        time.sleep(0.1)
if __name__ == "__main__":
 thread1=threading.Thread(target=task1)
 thread2=threading.Thread(target=task2)
 thread1.start()
 thread2.start()
 thread1.join()
 thread2.join()
 print("Both task completed")