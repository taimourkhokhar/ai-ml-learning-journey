# arr = [3, 1, 6, 2, 8, 4]

# prefix=[0] * len(arr)


# prefix[0]=arr[0]


# for i in range(1,len(arr)):
#   prefix[i]=arr[i-1]+arr[i]
  
# print(prefix)




# gain = [-5,1,5,0,-7]

# current=0
# altitude=0

# for g in gain:
#     current+=g
    
#     altitude=max(altitude,current)
# print(altitude)




#leeet code pivot index




# prefix=[0]*len(nums)

# prefix[0]=nums[0]

# for i in range(1,len(nums)):
#     prefix[i]=nums[i-1]+nums[i]
    
# print(prefix)
nums = [1,7,3,6,5,6]

totalsum=0

leftsum=0
rightsum=0
leftptr=0

for i in nums:
    totalsum+=i

for left in range(len(nums)):
    leftsum=sum(nums[:left])
    rightsum=sum(nums[left + 1:])
    if leftsum==rightsum:
        print(left)

