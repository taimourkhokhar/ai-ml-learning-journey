elements=[2,1,3,4,6,1,2]

def bubble(ele):
  size=len(ele)

  for k in range(len(elements)-1):
   swapped=False
   for i in range(size-1-k):
    if ele[i]>ele[i+1]:
      tmp=ele[i]
      ele[i]=ele[i+1]
      ele[i+1]=tmp
      swapped=True
    if not swapped:
      break




bubble(elements)
print(elements)