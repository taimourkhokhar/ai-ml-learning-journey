nums = [1,2,3,4]
k = 5
left=0
count=0
right=len(nums)-1
while left<right:
  sums=nums[left]+nums[right]
  if sums==k:
    count=count+1
    left+=1
    right-=1
  elif sums<k:
    left+=1
  else:
    right-=1

print(count)