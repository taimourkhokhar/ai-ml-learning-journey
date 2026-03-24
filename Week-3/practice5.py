#1 Create a list of cubes of numbers from 1 to 10.

# nums=[1,2,3,4,5,6,7,8,9,10]

# cubes=[y*y*y for y in nums ]
# print(cubes)


#From the list [12, 35, 47, 50, 86, 91], create a new list containing only numbers divisible by 5.


# nums=[12, 35, 47, 50, 86, 91]

# ans=[y for y in nums if y%5==0]

# print(ans)


#Given words = ["python", "java", "c++", "ruby"], create a list of word lengths.

# words=["python", "java", "c++", "ruby"]

# count=[len(x) for x in words ]

# print(count)


#Create a dict from words = ["apple", "banana", "cherry"] where key = word, value = word length.

# words=["apple", "banana", "cherry"]


# new={x:len(x) for x in words}
# print(new)

#From the list [10, 20, 30, 40], create a dict where key = number and value = "even" if divisible by 2, else "odd".

# num=[2,3,4,5,6,7,8]

# even_odd={x:"even" if x%2==0 else "odd" for x in num}

# print(even_odd)





#From the list [1,2,2,3,3,4,5,5], create a set of unique numbers multiplied by 2.


# num=[1,2,2,3,3,4,5,5]

# new={x*2 for x in num }
# print(new)




#From numbers 1-20, create a set of all even numbers.




# newone={x for x in range(1,21) if x%2==0}

# print(newone)




#From the list ["apple","banana","cherry","apple"], create a set of first letters.


# fruit=["apple","banana","cherry","apple"]


# new={x[0] for x in fruit}

# print(new)