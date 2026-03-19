import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {(end-start)*1000:.2f} ms")
        return result
    return wrapper


@ time_it

def calc_square(numbers):
  # start=time.time()
  result=[]
  for number in numbers:
    result.append(number*number)
  # end=time.time()
  # print("calc square took"+str((end-start)*1000)+"mil sec")
  return result

@time_it
def calc_cube(numbers):
  # start=time.time()

  result=[]
  for i in numbers:
    result.append(i*i*i)
  # end=time.time()
  # print("calc cube took"+str((end-start)*1000)+"mil sec")

  return result


array=range(1,1000)

out_square=calc_square(array)
out_cube=calc_cube(array)
print(len(out_square))
print((out_cube))