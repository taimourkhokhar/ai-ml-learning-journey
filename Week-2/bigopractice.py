# arr=[10,20,30,40]
# print(arr[2])
#even if array has 1million elements acceess through index is just one step
#for this O(1)


# arr=[10,20,30,40,50,60]
# for i in arr:
#   print(i)

#if input i mean array size increase loop run more 
# for this O(n)


# n=10
# for i in range(n):
#     for j in range(n):
#         print(i, j)

#if n=5 then 25 operation
#but if n=100 then 10000 operations
#so loops run double
#for this O(n^2)


# arr=[1,2,5,4,6,7,8]
# print(len(arr))
# target=6

# def binary_search(arr,target):
#    left=0
#    right=len(arr)-1
#    while left<=right:
#       mid=(left+right)//2
#       if arr[mid]==target:
#          return mid
#       elif arr[mid]<target:
#          left=mid+1
#       else:
#          right=mid-1

#    return -1


# print(binary_search(arr,target))



# #Array
# arr=[3,7,2,9,5]
# max=-1
# for i in arr:
#   if i>max:
#     max=i
# print(max)
#in this case it iterate from each element so that why O(n)


#create node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def print_list(head):
        temp=head
        while temp:
         print(temp.data)
         temp=temp.next
         
    def insert_begin(head,data):

    new_node = Node(data)

    new_node.next = head
    head = new_node

    return head


n1 = Node(10)
n2 = Node(20)

n1.next = n2

n1.print_list()

