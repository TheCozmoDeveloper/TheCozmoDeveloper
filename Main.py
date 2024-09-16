import random
import calendar
yy = 2024
mm = 5
def my_function():
  print("----------------------🅿🅾🆆🅴🆁🅴🅳 🅱🆈 🅿🆈🆃🅷🅾🅽----------------------")
  print("Hello,", Name, "Here is extra information that I've calculated for you:")
  print("Your PIN number is: ", PIN)
  print("Your password is: ", password)
  print("Today's date:", today)
  print("Current Time =", current_time)
  print("Thank you for using this program!")
  print("----------------------🅿🅾🆆🅴🆁🅴🅳 🅱🆈 🅿🆈🆃🅷🅾🅽----------------------")
#date and time
from datetime import date
today = date.today()
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("🅿🅾🆆🅴🆁🅴🅳 🅱🆈 🅿🆈🆃🅷🅾🅽")
print("~~Logging in~~")
print("~Logging in~")
Name = (input("What is your name? "))
print("It is nice to meet you,", Name)
password = (input("Please enter your Password: "))
PIN = int(input("Please enter your PIN number: "))
yy = int(input("Please enter the year you were born: "))
mm = int(input("Please enter the month you were born (number form): "))
print("Hello, ", Name, "This is your information:")
print(calendar.month(yy, mm))

response = input("Would you like me to print your entire year? (y/n) ")

#Prints
if response == "y":
  print("Okay, here is your calendar:")
  for i in range(1, 12):
    print(calendar.month(yy, i))
  response = input("Okay, would you like me to print a random month? (y/n) ")
  if response == "y":
    random_month = random.randint(1, 12)
    print("Okay, here is a random month:")
    print(calendar.month(yy, random_month))
    print("Thank you for using my program!")
  else:
    print("Okay, have a good day!")
elif response == "n":
  response = input("Okay, would you like me to print a random month? (y/n) ")
  if response == "y":
    random_month = random.randint(1, 12)
    print("Okay, here is a random month:")
    print(calendar.month(yy, random_month))

  else:
    print("Okay, have a good day!")

my_function()