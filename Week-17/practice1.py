name="Taimour"
age=23
city="Lahore"
print(f"My name is {name}, age is {age} and city is {city}")

a = 20
b = 5

print("sum is ",a+b)
print("subtraction is ",a-b)
print("multiplication is ",a*b)
print("division is ",a/b)

text = "Python"

print("p")
print("n")
print(text,text,text)

length = 10
width = 5


print("area of rectangle is ",length*width)


sentence = "I love machine learning"
count=0

for snt in sentence:
  count+=1



lwr=sentence.lower()
upr=sentence.upper()
print(count)
print(lwr)
print(upr)



#list
fruit=["mango","orange","apple","blueberry"]
print(fruit[0])
print(fruit[-1])

numbers = [10,20,30,40,50]
numbers.append(60)
print(numbers)

numbers = [5,10,15,20,25]

sum=0
for num in numbers:
  sum+=num

print("sum of numbers is ",sum)

names = ["Ali","Sara","Ahmed","Fatima"]

for name in names:
  print(name)

numbers = [1,2,3,4,5]

sume=[]

for num in numbers:
  sumer=num*num
  sume.append(sumer)

print(sume)