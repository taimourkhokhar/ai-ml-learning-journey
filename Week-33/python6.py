# str=["flower","flow","flight"]
# first_str=str[0]
# for i,char in enumerate(first_str):
#     for s in str[1:]:
#             if i==len(s) or s[i]!=char:
#                   print(first_str[:i])
# print(first_str)

ransomNote="aab"
magazine="baa"
ransomNote=list(ransomNote)
for i in list(ransomNote):
    if i in magazine:
        ransomNote.remove(i)
print(len(ransomNote))