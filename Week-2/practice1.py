##first with array

# arr=[10,20,30,40,50]
# print(arr[0])
# arr.append(15)
# print(arr)
# arr.pop()
# print(arr)
#for search O(N)

# for i in arr:
#   print(i)

  #hashtables

student={
    "name":"Taimour",
    "age":23,
    "School":"Apex"
  }
print(student["School"])



#stack last in first out

# stack=[]
# stack.append(15)
# stack.append(12)
# print(stack)
# stack.pop()
# print(stack)

#queue first in first out

# from collections import deque

# queue=deque()


# queue.append(5)
# queue.append(3)
# queue.append(2)
# print(queue)
# queue.popleft()
# print(queue)


#linked list
# class Node:
#   def __init__(self,data):
#     self.data=data
#     self.next=None





# n1=Node(10)
# n2=Node(20)
# n3=Node(30)

# n1.next=n2
# n2.next=n3



#double linked list


# class Node:
#   def __init__(self,data):
#     self.data=data
#     self.prev=None
#     self.next=None



##recusrion
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1)

# print(factorial(5))



#tree

# class Node:
#   def __init__(self,data):
#     self.data=data
#     self.left=None
#     self.right=None

# root =Node(10)
# root.left=Node(5)
# root.right=Node(15)
# root.left.left=Node(2)
# root.left.right=Node(7)
