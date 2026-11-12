# from multiprocessing import Process

# # def first():
# #     for _ in range(1,6):
# #         print(_)
# # def second():
# #     for _ in range(6,11):
# #         print(_)
# # if __name__ == "__main__":

# #  p1=Process(target=first)
# #  p2=Process(target=second)
# #  p1.start()
# #  p2.start()
# #  p1.join()
# #  p2.join()




# from multiprocessing import Pool
# def square(n):
#     return n*n
# if __name__=="__main__":
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     with Pool(processes=4) as pool:
#         result=pool.map(square,numbers)
#     print(result)


import time
import threading
import multiprocessing

# A simple CPU-bound task (heavy math loop)
def cpu_task():
    total = 0
    for i in range(15_000_000):
        total += i
    return total

if __name__ == "__main__":
    num_tasks = 4

    # 1. Normal Sequential Execution
    start = time.time()
    for _ in range(num_tasks):
        cpu_task()
    print(f"Sequential:     {time.time() - start:.2f} seconds")

    # 2. Multithreading Execution
    start = time.time()
    threads = [threading.Thread(target=cpu_task) for _ in range(num_tasks)]
    for t in threads: t.start()
    for t in threads: t.join()
    print(f"Multithreading: {time.time() - start:.2f} seconds (Blocked by GIL)")

    # 3. Multiprocessing Execution
    start = time.time()
    processes = [multiprocessing.Process(target=cpu_task) for _ in range(num_tasks)]
    for p in processes: p.start()
    for p in processes: p.join()
    print(f"Multiprocessing: {time.time() - start:.2f} seconds (True Parallelism)")