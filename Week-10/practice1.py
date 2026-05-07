s = "abciiidef"
k = 3
vow='aeiou'
count=0
max_count=count
for i in range(k):
  if s[i] in vow:
    count+=1

for i in range(k,len(s)):
  if s[i-k] in vow:
    count-=1
  if s[k] in vow:
    count+=1

  max_count=max(max_count,count)


print(max_count)
    


