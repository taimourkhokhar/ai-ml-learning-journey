# st="aadam"
# left=0
# right=len(st)-1
# while left<right:
#   if st[left]==st[right]:
#     print("Yes its plaindrom")
#     left+=1
#     right-=1
#   else:
    
#     print("not it not")
#     break

# import string
# s = "race a car"
# new=s.maketrans("","",string.punctuation)
# ch=s.translate(new).replace(" ","").lower()
# left=0
# right=len(ch)-1
# while left<right:
#   if ch[left]!=ch[right]:
#     print("not palindrom")
#   else:
#     left+=1
#     right-=1
# print("yes its palindrom")
  
height = [1,8,6,2,5,4,8,3,7]
max_value=0
left=0
right=len(height)-1
while left<right:
  width=right-left
  cur_height=min(height[left],height[right])
  area=cur_height*width
  max_value=max(max_value,area)
  if height[left]<height[right]:
    left+=1
  else:
    right-=1
print(max_value)