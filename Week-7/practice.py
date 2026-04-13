# num=[1,2,3,4,5]
# my=iter(num)
# print(next(my))
# print(next(my))
# print(next(my))
# print(next(my))
# print(next(my))
class CountUpTo:
  def __init__(self,n):
    self.n=n
    self.current=1
  def __iter__(self):
    return self
  def __next__(self):
    if self.current<=self.n:
      result=self.current
      self.current+=1
      return result
    else:
      raise StopIteration
counter=CountUpTo(5)

for num in counter:
  print(num)

