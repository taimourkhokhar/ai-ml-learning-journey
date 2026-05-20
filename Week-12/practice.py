# arr = [3, 1, 6, 2, 8, 4]

# prefix=[0] * len(arr)


# prefix[0]=arr[0]


# for i in range(1,len(arr)):
#   prefix[i]=arr[i-1]+arr[i]
  
# print(prefix)




gain = [-5,1,5,0,-7]

current=0
altitude=0

for g in gain:
    current+=g
    
    altitude=max(altitude,current)
print(altitude)