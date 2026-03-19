import time
import multiprocessing
square_result=[]
def cal_square(numbers):
  global square_result
  print("Calculate square of numbers")
  for n in numbers:
    # time.sleep(5)
    print('square',str(n*n))
    square_result.append(n*n)
  print('within process result'+str(square_result))


# def cal_cube(numbers):
#   print("Calculate cube of numbers")
#   for n in numbers:
#     time.sleep(5)
#     print('cube',n*n*n)


if __name__=="__main__":
  arr=[2,3,8,9]

  p1=multiprocessing.Process(target=cal_square,args=(arr,))

  # p2=multiprocessing.Process(target=cal_cube,args=(arr,))




  p1.start()
  # p2.start()


  p1.join()
  # p2.join()


  print('result'+str(square_result))

  print("Done!")