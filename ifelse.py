# user_input=int(input())
# if user_input%2==0:
#   print("user number is even")
# else:
#   print("user number is odd")


# user_dish=input("Enter a dish name")
# if user_dish=="saag"or"karahi gosht":
#   print("cuisines is Regional flavor")
# elif user_dish=="biryani" or "tikka massala":
#   print("cuisines is signature dish")
# else:
#   print("cultural context ")


#cuisine program

# indian=["samosa","daal","naan"]
# chinese=["egg role","pot sticker","fried rice"]
# italian=["pizza","pasta","risotto"]

# dish=input("Enter a dish name")

# if dish in indian:
#   print("indian cuisine")
# elif dish in chinese:
#   print("chinese cuisine")
# elif dish in italian:
#   print("italian cuisine")
# else:
#   print("we dont know ")


  #prime number
num = int(input())

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a prime number")