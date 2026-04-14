# num=[1,2,3,4,5]
# my=iter(num)
# print(next(my))
# print(next(my))
# print(next(my))
# print(next(my))
# print(next(my))
# class CountUpTo:
#   def __init__(self,n):
#     self.n=n
#     self.current=1
#   def __iter__(self):
#     return self
#   def __next__(self):
#     if self.current<=self.n:
#       result=self.current
#       self.current+=1
#       return result
#     else:
#       raise StopIteration
# counter=CountUpTo(5)

# for num in counter:
#   print(num)

# str1="taimour"
# str2=list(str1)
# str2.reverse()
# new="".join(str2)
# my=iter(new)
# print(next(my))
# print(next(my))
# print(next(my))
# print(next(my))

# print(str[::-1])
# for i in str1:
#   print(i)


# 3. Even Numbers Iterator

# Create a class that:

# Takes a limit n
# Iterates only even numbers up to n

# 👉 Example:

# n = 10 → 2,4,6,8,10

# class Even:
#   def __init__(self,n):
#     self.n=n
#     self.current=1
#   def __iter__(self):
#     return self
#   def __next__(self):
#     if self.current<=self.n:
#       res=self.current
#       self.current+=1
#       val=res%2==0
#       return val
#     else:
#       raise StopIteration
# n=10
# nw=Even(n)
# for i in nw:
#   print(i)

# f=open("D:/ai engineer roadmap/funny.txt",'r')
# new=f.read()
# f.close()
# nw=iter(new.splitlines())
# print(next(nw))
# print(next(nw))

# marks = {"Ali": 85, "Sara": 92, "John": 78, "Ayesha": 88}

# print(max(marks))

# avg=0

# for key,val in marks.items():
#   avg+=val
#   length=len(marks)
#   ans=avg/length
#   print(ans)


# marks["Taimour"]=95
# print(marks)

# from collections import Counter

# text = "apple banana apple orange banana apple"

# ans=Counter(text.split())
# print(ans)

# text = "apple banana apple orange banana apple"
# words=text.split()
# print(words)
# dic={}
# for word in words:
#    if word in dic:
#       dic[word]+=1
#    else:
#       dic[word]=1

# print(dic) 

# dict1 = {"a": 10, "b": 20}
# dict2 = {"b": 5, "c": 15}

# merge=dict1.copy()

# for i,v in dict2.items():
#   if i in merge:
#     merge[i]+=v
#   else:
#     merge[i]=v

# print(merge)
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# inverted={value:key for key,value in my_dict.items()}
# print(inverted)



  





