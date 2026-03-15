#find the maximum in this array
# arr=[4,2,9,1]
# max=-1

# for i in arr:
#   if i>max:
#     max=i
# print(max)
#revers of array




# def reverse_array(arr):
#   left=0
#   right=len(arr)-1

#   while left<right:
#     arr[left],arr[right]=arr[right],arr[left]
#     left+=1
#     right-=1
#   return arr


# print(reverse_array(arr))

#find element in array
# arr=[4,2,9,1]

# find=10
# for i in arr:
#   if i==find:
#    print(i,"is present in array")
#   else:
#     print("Number is not preset in array")


#stack all important operations

# class Stack:
#   def __init__(self):
#     self.stack=[]

#   def push(self,data):
#     self.stack.append(data)

#   def pop(self):
#     if st.is_empty():
#       return
#     self.stack.pop()

#   def peek(self):
#     return self.stack[-1]
#   def is_empty(self):
#     if len(self.stack)==0:
#       print("stack is empty fill it first")
  
#   def display(self):
#     for i in self.stack:
#       print(i)


# st=Stack()

# st.push(5)
# st.push(4)
# st.push(2)
# st.display()
# print(st.peek())
# # st.pop()

# from collections import deque
# class Queue:
#   def __init__(self):
#    self.deq=deque()

#   def push(self,data):
#     self.deq.append(data)

#   def Deque(self):
#     if self.is_empty():
#       return
#     self.deq.popleft()

#   def show(self):
#     for i in self.deq:
#       print(i)

#   def peek(self):
#     return self.deq[-1]
  
#   def is_empty(self):
#     if len(self.deq)==0:
#       print("Queue is empty")

# q=Queue()
# # q.push(5)
# # q.push(6)
# # q.push(7)
# q.Deque()
# # print(q.peek())
# # q.show()


#linked list practice

# class Node:
#     def __init__(self, data):
#        self.data = data
#        self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def insert_at_begin(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     def show_all(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")

#     def search(self,ele):
#         current=self.head
#         while current:
#             if ele == current.data:
#                 print("element present")
#                 return True
#             current=current.next
#         print("Element not preseent")
#         return False
                
               

# ll = LinkedList()
# ll.insert_at_begin(11)
# ll.insert_at_begin(12)
# ll.insert_at_begin(13)

# print(ll.search(55))

# ll.show_all() 
# def factorail(n):
#   if n==1:
#     return n
#   return n*factorail(n-1)

# print(factorail(5))




#tree

