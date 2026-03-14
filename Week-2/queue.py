stock_price_queue=[]


stock_price_queue.insert(0,132)
stock_price_queue.insert(0,122)
stock_price_queue.insert(0,111)


#132 will remove becasue queue is first in first out fifo approach
stock_price_queue.pop()


print(stock_price_queue)





from collections import deque

q=deque()


q.appendleft(5)
q.appendleft(3)
q.appendleft(4)


q.pop()

print(q)




class Queue:
  def __init__(self):
    self.buffer=deque()

  def enqueu(self,val):
    self.buffer.appendleft(val)

  def deque(self):
    return self.buffer.pop()
  
  def is_empty(self):
    return len(self.buffer)==0
  
  def size(self):
    return len(self.buffer)