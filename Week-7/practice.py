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

f=open("D:/ai engineer roadmap/funny.txt",'r')
new=f.read()
f.close()
nw=iter(new.splitlines())
print(next(nw))
print(next(nw))