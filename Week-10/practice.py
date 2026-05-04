nums = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
k = 2

nums.sort() 

left = 0
right = len(nums) - 1
count = 0

while left < right:
    sums = nums[left] + nums[right]
    
    if sums == k:
        count += 1
        left += 1
        right -= 1
    elif sums < k:
        left += 1
    else:
        right -= 1

print(f"Pairs found: {count}")