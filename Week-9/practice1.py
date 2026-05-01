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

import string
s = "race a car"
new=s.maketrans("","",string.punctuation)
ch=s.translate(new).replace(" ","").lower()
left=0
right=len(ch)-1
while left<right:
  if ch[left]!=ch[right]:
    print("not palindrom")
  else:
    left+=1
    right-=1
print("yes its palindrom")
  
