#this is standarad exception
# try:
#   raise MemoryError("memory eror")
# except MemoryError as e:
#   print(e)



#own exception class


class Accident(Exception):
  def __init__(self,msg):
    self.msg=msg

  def print_exception(self):
    print("Use defined exception  ",self.msg)


try:
  raise Accident("crach between cars")
     
except Accident as e:
  print(e.print_exception())




 #finally term that is run on both condition 