f=open("D://data//funny.txt","w")

f.write("I love python")

f.close()


O=open("D://data//funny.txt","r")
for line in O:
  tokens=line.split(' ')
  print(str(tokens))
  print(len(tokens))
O.close()
