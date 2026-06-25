# num=5
# if num>=0:
#   print("positive")
# else:
#   print("negative")

# nums=6
# if nums%2==0:
#   print("even numbers")
# else:
#   print("odd")
  
  
# age=18
# if age>=18:
#   print("You are eligible for voting")
# else:
#   print("You are not eligible for voting")

# num1=2
# num2=3
# if num1>num2:
#   print(num1)
# else:
#   print(num2)

# marks=50
# if marks>=50:
#   print("pass")
# else:
#   print("fail")

# nums=10
# for i in range(1,nums+1):
#   print(i)


# for i in range(1,20):
#   if i%2==0:
#     print(i)

# sum=0
# for i in range(1,100):
#   sum+=i
# print(sum)

# num=5
# for i in range(1,11):
#   print(f"5 *{i}",num*i)


# text="machinelearning"
# count=0

# for i in text:
#  if i in "aeiou":
#   count+=1
  
# print(count)


# def hello():
#   print("hello python")

# hello()

# def add(a,b):
#   print(a+b)
# add(10,20)

# def square(a):
#   print(a*a)
# square(10)

# squares=lambda x:x*x
# print(squares(5))


# add=lambda x,y:x+y
# print(add(5,5))

# even=lambda num:"even" if num%2==0 else "odd"
# print(even(5))


# numbers = [1,2,3,4,5]

# square=list(map(lambda num:num*num,numbers))
# print(square)

# even=list(filter(lambda x:x%2==0,numbers))
# print(even)



students = [
    {"name":"Ali","marks":85},
    {"name":"Sara","marks":92},
    {"name":"Ahmed","marks":78},
    {"name":"Fatima","marks":95}
]


for key in students:
  print(key["name"])
  
maximum=[]
for key in students:
  maximum.append(key["marks"])
  
print(max(maximum))

sum=0
for i in maximum:
  sum=sum+i
print("average student score is",sum/len(maximum))
  
  
for key in students:
  if key["marks"]>90:
    print(key["name"])
    
sorted_student=sorted(students,key=lambda student:student["marks"],reverse=True)
for st in sorted_student:
  print(st)