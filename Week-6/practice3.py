# from collections import Counter
# chars = ["a","b","b","c","c","c"]
# count=Counter(chars)
# string=str(count)
# new="".join(string)
# print(new)


# my_list = ["a","b","b","c","c","c"]

# count = {}

# for item in my_list:
#     if item in count:
#         count[item] += 1
#     else:
#         count[item] = 1

# print(count)

# from collections import Counter

# my_list = ['a', 'b', 'a', 'c', 'b', 'a', 'd']

# count = Counter(my_list)

# for key, value in count.items():
#     if value == 1:
#         print(key)
#     else:
#         print(f"{key}: {value}")

# my_list = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# result=''
# for ch in set(my_list):
#   count=my_list.count(ch)
#   if count>1:
#     result+=ch+str(count)
#   else:
#     result+=ch

# print(len(result))


# counter=[1,2,2,3]
# count={}
# for i in counter:
#   if i in count:
#     count[i]+=1
#   else:
#     count[i]=1

# print(count)
# from collections import Counter

# counter=[1,2,2,3]
# new=Counter(counter)
# print(new)

str1 = "ABCABC"
str2 = "ABC"
# def repeat(s):
#  seen=set()
#  for i in s:
#   if i in seen:
#    return i
#   seen.add(i)
#  return None

# print(repeat(str1))

# def check(str1,str2):
#  dup=[char for char in set(str1) if str1.count(char)>1]
#  if not dup:
#   return ""
#  new="".join(dup)
#  if new in str2:
#   return new
#  else:
#   return ""

# print(check(str1,str2))