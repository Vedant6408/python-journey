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

# #Find the largest of three number
# x, y, z = 1, 20, 400
# # print(f"{max(x,y,z)} is larger number.")

# if x > y and x > z:			#if x > y is true, x > z true then absolutely x is larger number, if not then z and y will be greater
# 	print("x is greater")	#now if we compare z and y then we'll get the answer who is greater, if we got false here then absolutely z is greater as you can see at else
# elif y > z:							#i solve this question from scratch
# 	print("y is greater")
# else:print("z is greater")

#Check if a year is leap year
# usr_input = int(input('ENTER YEAR: '))
# if usr_input%4 == 0:
# 	print(f"This {usr_input} is leap year")
# else:print(f"this {usr_input} isn't a leap year")

# #check if a character is an alphabet, digit or special character
usr_inp = input("ENTER ANY CHARACTER:: ")
# #let's check these character is what? without using in-built function
# if usr_inp.upper() in ("A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"):print("YOU ENTERED ALPHABET")
# # elif usr_inp in ["1,2,3,4,5,6,7,8,9,0"]:print("ENTERED NUMBERS") #here compiler check usr_inp in whole string which is just one element
# elif usr_inp in ("1,2,3,4,5,6,7,8,9,0"):print("ENTERED NUMBERS")  #this isn't exactly a tuple but here compiler check substring that's why it's will return right value
# else:print(" your entered some special CHARACTER")
# #here is the problem in this program user only have to enter one character otherwise it's return else statement.......
#now let's make this using in-built function
if usr_inp.isdigit():print("your enetered numbers")
elif usr_inp.isalpha():print("your eneterd alphabet")
else:
	print("You eneterd special CHARACTER")
	