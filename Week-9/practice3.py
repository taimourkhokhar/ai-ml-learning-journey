s = "abc"
t = "ahbgdc"
def checker(s,t):
 sleft=0 
 tleft=0
 while sleft<len(s) and tleft<len(t):
  if s[sleft]==t[tleft]:
    sleft+=1
  tleft+=1
 return sleft==len(s)


print(checker(s,t))