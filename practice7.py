india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]


# Write a program that asks user to enter a city name and it should tell which country the city belongs to
# user=input("Enter a city name")

# if user in india:
#   print("City is in India")
# elif user in pakistan:
#   print("City is in pakistan")
# elif user in bangladesh:
#   print("City is in Bangladesh")
# else:
#   print("You input a invalid city")


# city1 = input("Enter city 1: ")
# city2 = input("Enter city 2: ")

# if city1 in india and city2 in india:
#     print("Both cities are in india")
# elif city1 in pakistan and city2 in pakistan:
#     print("Both cities are in pakistan")
# elif city1 in bangladesh and city2 in bangladesh:
#     print("Both cities are in bangladesh")
# else:
#     print("They don't belong to same country")

# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

# count=0
# for i in result:
#   if i=='heads':
#     count=count+1
#     print(count)

for i in range(1,11):
  if i%2==1:
    print(i*i)


expense_list = [2340, 2500, 2100, 3100, 2980]

expense=int(input("Enter a expense"))

for i in expense_list:
  if expense==expense_list[0]:
    print("month is jan")
    break
  elif expense==expense_list[1]:
    print("Month is feb")
    break
  elif expense==expense_list[2]:
    print("Month is march")
    break
  elif expense==expense_list[3]:
    print("month is april")
    break
  elif expense==expense_list[4]:
    print("Month is may")
    break
  else:
    print("Your input is worng")