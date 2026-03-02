expense=[2340,2500,2100,3100,2980]
# total=expense[0]+expense[1]+expense[2]+expense[3]+expense[4]
# print(total)  

total=0
for item in expense:
  total=total+item
print(total)


# num=[1,2,3,4,5,6,7,8,9,10]

# for nums in range(1,11):
#   print(nums)

for i in range(len(expense)):
  print("month",(i+1),'Expense',expense[i])
  total=total+expense[i]

print('Total',total)



key_location="chair"
locations=["garage","living room","closet","chair"]

for i in locations:
  if i==key_location:
    print("key is found in ",i)
    break
  else:
    print("key is not found in ",i)


nums=[1,2,3,4,5]

for i in range(1,6):
  if i%2==1:
    print(i*i)
  else:
    print("i am ok bro")


j=1
while j<=5:
  print(j)
  j+=1