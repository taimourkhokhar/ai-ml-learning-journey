# haystack="hello"
# needle="ll"
# indexes=[]
# for i in range(1,len(needle)-1):
#  if needle in haystack:
#     print(haystack.index(needle))
ls=[1,2,3,4,5,6]

# def mean(ls):
#     value=0
#     for i in ls:
#         value+=i
#     print("Mean of this list is ", value/len(ls))
# mean(ls)
def median(ls):
  value=0
  if len(ls)%2==0:
     value=sum(ls)
     print((value+1)/len(ls))
  else:
     value=sum(ls)
     print(value/len(ls))
median(ls)

def range(ls):
   print(max(ls)-min(ls))
range(ls)