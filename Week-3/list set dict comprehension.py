#list comprehension 

# numbers=[1,2,3,4,5,6,7]

# even=[i for i in numbers if i%2==0]


# print(even)


# square=[i*i for i in numbers]
# print(square)

#set comprehension

s=set([1,2,3,4,5,2,3])
print(s)

even={i for i in s if i%2==0}
print(even)


#dict comprehension

cities=["mumbai","new york","paris"]

countire=["India","usa","france"]


z=zip(cities,countire)

for i in z:
  print(i)


d={city:countire for city,countire in zip(cities,countire)}


print(d)