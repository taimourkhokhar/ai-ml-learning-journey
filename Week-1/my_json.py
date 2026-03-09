import json as json


book={}

book['tom']={
  'name':'tom',
  'address':'1 purple street nyc',
  'phone':45461231
}


book['bob']={
  'name':'bob',
  'address':'1 orange street nyc',
  'phone':45461231
}




s=json.dumps(book)


with open("D://data/book.txt","w") as f:
  f.write(s)

#open and read
f=open("D://data/book.txt","r")

f=f.read()

print(f)




again_dec=json.loads(f)
print(again_dec)

print(type(f))
print(type(again_dec))
