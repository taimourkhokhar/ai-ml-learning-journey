# s=[]

# s.append('https://www.cnn.com/')
# s.append('https://www.cnn.com/world')
# s.append('https://www.cnn.com/india')
# s.append('https://www.cnn.com/china')
# s.append('https://www.cnn.com/usa')
# s.pop()
# print(s)
from collections import deque

# print(dir(deque))

class Stack:
  def __init__(self):
    self.container=deque()

  def push(self,val):
    self.container.append(val)

  def pop(self):
    return self.container.pop()
  
  def peek(self):
    return self.container[-1]
  
  def isempty(self):
    return len(self.container)==0
  
  def size(self):
    return len(self.container)
  


s=Stack()
s.push(5)


print(s.peek())
