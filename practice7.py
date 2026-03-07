india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]


# Write a program that asks user to enter a city name and it should tell which country the city belongs to
user=input("Enter a city name")

if user in india:
  print("City is in India")
elif user in pakistan:
  print("City is in pakistan")
elif user in bangladesh:
  print("City is in Bangladesh")
else:
  print("You input a invalid city")