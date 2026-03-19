# basket={"orange","apple","mango","apple"}

# print(basket)

# numbers=[1,2,3,4,5,6,7,6,8,9]
# unique_numbers=set(numbers)
# print(unique_numbers)


# #frozen set

# fs=frozenset(numbers)
# print(fs)


#basice operation like union intersetion difference like

set1={1,2,3,4,5}
set2={2,3}

set3=set1.union(set2)



print(set3)
print(set1.difference(set2))
print(set1.intersection(set2))
print(set2.issubset(set1))