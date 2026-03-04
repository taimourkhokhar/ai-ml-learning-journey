# with open("D://data//new.txt","w") as f:
#   for i in range(5):
#     name=input("Enter a name")
#     f.write(name)



# with open("D://data//new.txt","r") as R:
#     content=R.read()
#     print("Names in files")
#     print(content.upper())


import json

products=[
      {"name": "Laptop", "price": 1000, "quantity": 3},
    {"name": "Phone", "price": 500, "quantity": 5},
    {"name": "Headphones", "price": 100, "quantity": 10}
]

with open("D://ai engineer//new.txt","w") as f:
  json.dump(products,f,indent=4)

print("products saved successfully")



#load back from file
with open("D://ai engineer//new.txt","r") as f:
  loaded_product=json.load(f)

total=0
for i in loaded_product:
   total+=i["price"]*i["quantity"]
print("Total invenctory value",total)