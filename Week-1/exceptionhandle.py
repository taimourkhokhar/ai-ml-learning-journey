x=input("Enter a number")
y=input("Enter a number2")
try:
 z=int(x)/int(y)
except Exception as e:
 z=None
 print('exception occur',e)
print("Division is:",z)
