#In this code we're gonna try conditional statements in python
# age = int(input("Enter your age: "))
# if age >= 19 and age <= 40:
#     print("You're eligible for that examination")
# elif age > 40:
#     print("You've to rest now")
# elif age >= 14 and age < 19:
#     print("you can do part time job")
# else:
#     print("You're a kid, enjoy your childhood")
        
#Now we're gonna make simple program for checking whether user can apply for driving license or not
# age2 = int(input("Enter your age: "))
# if(age2 >= 18):
#  print("You can apply for driving license")
# elif(age2 < 18):
#   print("You can't apply for driving license")
# else:
#  print("Invalid input or try again")

a = int(input("Enter you age: "))
if a >= 18:
    if a >= 70:
        print("You can't drive on road Because of your age")
    else:
      print("You can safely drive on road")
else:
    print("You can't drive on road")