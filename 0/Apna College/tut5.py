# WAP a program to check whether a number is odd or even
num = int(input("Enter a number: "))
if((num%2)==0):
    print("The number you've entered is Even")
else:
    print("The number you've entered is Odd")

# WAP a program to check the greatest number entered by the user
# This program only work on different values of all these three number if 2 of them are same than it will not work 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input('Enter third number: '))
if(num1 >= num2 and num1 >= num3):
    print("First number is the greatest number")
elif(num2 > num3):
    print("Second number is the greatest number")
elif(num1 == num2 and num2 == num3):
    print("All numbers are equal")
else:
    print("Third number is the greatest number")


# WAP to check the entered by users are the multiple of 7 or not
inp = int(input('enter your number'))
if((inp%7)==0):
    print("Your entered value is multiple of 7")
else:
    print("not a multiple of 7")

print("Multiplaying complex number", (1 + 7j)*(1 - 7j))

