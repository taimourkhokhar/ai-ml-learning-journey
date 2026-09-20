# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("Emil", 36)

# print(p1.name)
# print(p1.age)

# class Person:
#   pass

# p1 = Person()
# p1.name = "Tobias"
# p1.age = 25

# print(p1.name)
# print(p1.age)


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("Linus", 28)

# print(p1.name)
# print(p1.age)


# class Person:
#   def __init__(self, name, age=18):
#     self.name = name
#     self.age = age

# p1 = Person("Emil")
# p2 = Person("Tobias", 25)

# print(p1.name, p1.age)
# print(p2.name, p2.age)

# class Person:
#   def __init__(self, name, age, city, country):
#     self.name = name
#     self.age = age
#     self.city = city
#     self.country = country

# p1 = Person("Linus", 30, "Oslo", "Norway")

# print(p1.name)
# print(p1.age)
# print(p1.city)
# print(p1.country)

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# word1="abc" 
# word2="pqr"
# mergerd=[]
# for i , j in zip(word1,word2):
#     mergerd.append(i)
#     mergerd.append(j)
# print("".join(mergerd))

# Input: word1 = "ab", word2 = "pqrs"
word1="pqrs"
word2="ab"
merged=[]    
for i,j in zip(word1,word2):
   merged.append(i)
   merged.append(j)
   remain=min(len(word1),len(word2))
   remain=word2[2:] or word1[2:]
print("".join(merged)+remain)
