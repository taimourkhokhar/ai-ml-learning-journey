# # # # Input: nums = [0,0,1,1,1,2,2,3,3,4]
# # # # Output: 5
# # # #brute force approach
# # # nums=[1,1,2]
# # # out=[]
# # # for i in nums:
# # #     if i not in out:
# # #         out.append(i)

# # # print(len(out))


# # # class Solution:
# # #     def removeDuplicates(self, nums: list[int]) -> int:
# # #         out = []
# # #         for i in nums:
# # #             if i not in out:  # Fixed: check 'out', not 'nums'
# # #                 out.append(i)
        
# # #         nums[:] = out
        
# # #         # Return the integer count of unique elements
# # #         return len(nums)

# # import threading
# # import time
# # # def task1():
# # #     for i in range(1,6):
# # #         print(i)
# # #         time.sleep(0.1)
# # # def task2():
# # #     for letter in ['a','b','c','d','e']:
# # #         print(letter)
# # #         time.sleep(0.1)
# # # if __name__ == "__main__":
# # #  thread1=threading.Thread(target=task1)
# # #  thread2=threading.Thread(target=task2)
# # #  thread1.start()
# # #  thread2.start()
# # #  thread1.join()
# # #  thread2.join()
# # #  print("Both task completed")


# # import time
# # import threading

# # def downloading1():
# #     print("Downloading 1 file")
# #     time.sleep(2)

# # def downloading2():  # Fixed typo here
# #     print("Downloading 2 file")
# #     time.sleep(2)

# # def downloading3():
# #     print("Downloading 3 file")
# #     time.sleep(2)


# # # --- 1. Sequential Execution ---
# # print("--- Sequential Execution ---")
# # start_seq = time.time()

# # downloading1()
# # downloading2()
# # downloading3()

# # end_seq = time.time()
# # sequential_time = end_seq - start_seq
# # print(f"Sequential time: {sequential_time:.2f} seconds\n")


# # # --- 2. Concurrent Execution (Your Threads) ---
# # print("--- Concurrent Execution ---")
# # start_conc = time.time()

# # thread1 = threading.Thread(target=downloading1)
# # thread2 = threading.Thread(target=downloading2)
# # thread3 = threading.Thread(target=downloading3)

# # thread1.start()
# # thread2.start()
# # thread3.start()

# # thread1.join()
# # thread2.join()
# # thread3.join()

# # end_conc = time.time()
# # concurrent_time = end_conc - start_conc
# # print(f"Concurrent time: {concurrent_time:.2f} seconds\n")


# # # --- 3. Comparison ---
# # print(f"Comparison Result:")
# # print(f"Sequential took ~{sequential_time:.0f} seconds (files downloaded one after another).")
# # print(f"Concurrent took ~{concurrent_time:.0f} seconds (files downloaded at the same time).")

# import threading
# counter=0
# def increment_without_lock():
#     global counter
#     for _ in range(100000):
#         counter+=1
# t1=threading.Thread(target=increment_without_lock)
# t2=threading.Thread(target=increment_without_lock)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(f"Final counter WITHOUT lock: {counter} (Expected: 200000)")

# counter=0
# lock=threading.lock()

# def increment_with_lock():
#     global counter
#     for _ in range(100000):
#         with lock:
#             counter==1
# t3 = threading.Thread(target=increment_with_lock)
# t4 = threading.Thread(target=increment_with_lock)

# t3.start()
# t4.start()
# t3.join()
# t4.join()

# print(f"Final counter WITH lock: {counter} (Expected: 200000)")

