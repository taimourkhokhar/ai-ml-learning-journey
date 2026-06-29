with open("name.txt","w") as file:
  file.write("Hello everyone welcome to Python")

count=0  
with open("name.txt","r") as file:
  read=file.read()
  for rd in read.split():
    count+=1
    
print(count)

 