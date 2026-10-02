import math
# x = 9
# y = 9.1
# z = 9.9

# result = math.sqrt(x)
# #math.ceil function round off greatest vaule
# result2 = math.ceil(y)
# #math.floor functin round off to the lowest value
# result3 = math.floor(z)
# print(f"The round off of z is: {result3}")
# print(f"The round off of y is: {result2}")
# print(f"The square root of x is: {result}")

#Exercise 1 finding the circumference of a circle
# userinp = float(input("Enter the radius of a circle: "))
# circum = 2 * userinp * math.pi  
# print(f"The circumference of a circle is {round(circum, 3)}cm")

#Exercise 2 Calculate the area of a circle

# userinp2 = float(input("Enter the radius of a circle: "))
# area_of_circle = math.pi * userinp2 ** 2
# print(f"The Area of a square is {round(area_of_circle, 2)}w")

#Exercise 3 Calculate the hypotenuse of a triangle whose 2 sides are given
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
hypo = math.sqrt(pow(a, 2) + pow(b, 2))
print("The hypotenuse of a triangle is: ", hypo)