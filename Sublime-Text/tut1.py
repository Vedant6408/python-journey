# #check number if positive or negative
# inp1 = int(input("ENTER ANY NUMBER:: "))
# if inp1 < 0:
# 	print("YOU ENTERED NEGATIVE NUMBER.")
# elif inp1 > 0:
# 	print("YOU ENTERED POSITIVE NUMBER. ")
# elif inp1 == 0:
# 	print("This nor POSITIVE nor NEGATIVE")
# else:
# 	print("syntax error !!")

# #determine if an interger is odd or even
# inp2 = int(input("ENTER ANY NUMBER:: "))
# if inp2%2 == 0:
# 	print("YOU ENTERED EVEN NUMBER")    #sometimes  inp2/2 == 0: comparison in if else statement gives right output
# elif inp2%2 != 0:
# 	print("You ENTERED ODD NUMBER")
# else:
# 	print("SYNTAXX ERRORR !")


# #check divisibility by 5 and 11
# inp3 = int(input("enter any number:: "))
# if inp3%5 == 0 and inp3%11 == 0:
# 	print("This number is divisible by both")
# else:
# 	print("isn't divisible")

# #Find the largest of two number
# num1 = int(input("First num:: "))
# num2 = int(input("Second num:: "))
# # if num1 > num2: print("num1 is larger")
# # else: print("num2 is larger")
# #using ternary operator
# print("num1 is larger" if num1 > num2 else "num2 is larger")
# #using max function
# print(f"The larger number is: {max(num1,num2)}")

#Find the largest of three number
x, y, z = 1, 20, 400
# print(f"{max(x,y,z)} is larger number.")

if x > y and x > z:			#if x > y is true, x > z true then absolutely x is larger number, if not then z and y will be greater
	print("x is greater")	#now if we compare z and y then we'll get the answer who is greater, if we got false here then absolutely z is greater as you can see at else
elif y > z:							#i solve this question from scratch
	print("y is greater")
else:print("z is greater")