# type: ignore
import pyttsx3
# #logical operators
# print(not True)
# print(not False)

# #it means these logical operators return opposite of the value 
# a = 18 
# b = 19 
# print(not (a > b)) #it will return opposite of the value of a > b

# #And operator
# c = True 
# d = True
# print( c and d )

# #or Operator

# e = False
# f = False
# print(e or f)
# print("Or Operator:", (a==b) or (c and d))

#Type conversion
# a = int("18")
# b = 2.45
# print(type(a))
# print(a + b) 

#WAP to input two numbers and print their sum, difference, product and quotient
# val1 = int(input("Enter First Number:"))
# num2 = int(input("Enter Second number:"))
# print("Sum:", val1 + num2)
# print("Their Difference:", val1 - num2)
# print("product:", val1*num2)
# print("Quotient:", num2/val1)

#WAP to input a side of square and print its area and perimeter
# inpside = int(input("Enter the side of square:"))
# print("Area of Square:", (inpside)**2) #** is the power operator
# print("Perimeter of Square:", 4*inpside)

#WAP to input two floats and print their avg.
val1 = float(input("Enter first number:"))
val2 = float(input('Enter second number:'))
# val3 = print("Average of two numbers:", (val1 + val2)/2)
def avgoftwo(a, b):
    return (a + b)/2


def1 = avgoftwo(val1, val2)
print("Average of two numbers is ", def1)


engine = pyttsx3.init()
engine.say("Average of two numbers is " + str(def1))
engine.runAndWait()



