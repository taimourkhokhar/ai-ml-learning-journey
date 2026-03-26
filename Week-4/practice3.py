#4 Count how many times each element appears frequency

# nums=[1,2,2,3,4]
# new=[]
# for i in nums:
#   if i not in new:
#     new.append(i)
#     count=nums.count(i)
#     print(count)
# print(new)

# nums=[1,2,3,4,4]
# freq={}
# for i in nums:
#   if i in freq:
#     freq[i]+=1
#   else:
#     freq[i]=1
# print(freq)



#Rotate a list to the right by k steps

# nums=[1,2,3,4]
# step=2
# for i in range(step):
#  last=nums.pop()
#  nums.insert(0,last)
# print(nums)

cand=[2,3,5,1,3]
ext=3
val=[]

def Candies(cand,ext):
  for i in cand:
    val.append(i+ext)

  min=val[-1]
  final=[]
  for i in val:
    if i<min:
      min=i
      ans="false"
      final.append(ans)
    else:
      anse="true"
      final.append(anse)
  print("minimum is",min)
  
  


Candies(cand,ext)