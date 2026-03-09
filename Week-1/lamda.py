add=lambda x,y:x+y
print(add(2,3))


is_even=lambda x:x%2==0
print(is_even(3))


#filter 

numbers=[1,2,3,4,5,6,7,8]

even=list(filter(lambda x:x%2==0,numbers))

print(even)


numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared) 
