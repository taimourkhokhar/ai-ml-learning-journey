word1 = "ab"
word2 = "pqrs"
merge=[]
# count1=len(word1)
# count2=len(word2)
# print(count1,count2)
# count=0
# for i in zip(word1,word2):
#    if len(word1)<len(word2):
#     merge.extend(i)
# final="".join(merge)
# print(final)

for char1,char2 in zip(word1,word2):
  merge.append(char1)
  merge.append(char2)
remainig=min(len(word1),len(word2))
remainig=word1[remainig:]+word2[remainig:]
result="".join(merge)+remainig
print(result)