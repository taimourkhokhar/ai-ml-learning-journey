nums = [1,12,-5,-6,50,3,4,10]
k=4
windowsum=sum(nums[:k])
maxsum=windowsum

for i in range(k,len(nums)):
  windowsum=windowsum-nums[i-k]+nums[i]
  if windowsum>maxsum:
    maxsum=windowsum
    
print(maxsum)