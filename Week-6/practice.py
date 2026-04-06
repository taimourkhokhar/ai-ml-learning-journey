# word1="abc"
# word2="pqr"

# new=list(word1)
# new.insert(5," ")

# new_str="".join(new)

# print(new_str)

# word1="abc"
# word2="pqr"
# new=""
# len1=len(word1)
# len2=len(word2)
# len3=len1+len2
# print(len3)
# # for m in range(len3):
# for i,j in word1,word2:
#     new+=i+j
# print(new)

# word1 = "abc"
# word2 = "pqr"
# new = ""

# # Since both are length 3, we can loop through the range of the length
# for i in range(len(word1)):
#     new += word1[i] + word2[i]

# print(new) 
# Output: apbqcr
# new=""
# word1="abcd"
# word2="pq"
# for i in range(len(word1)):#i have 3
#   new+=word1[i]+word2[i]
# print(new)


word1="abcd"
word2="pq"
result=""
max_length=max(len(word1),len(word2))
#here we choose max lenght to sure htat loop iterate max time may be word1 or word2
for i in range(max_length):
#here it run by max 4 due to word1
  if i<len(word1):#first 1 less than 4 then it add a to the result then move forward
    result+=word1[i]
  if i<len(word2):#here same like first 
    result+=word2[i]
print(result)   