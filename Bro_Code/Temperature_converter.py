#Temperature conversion program using python 
unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the Temperature: "))
if unit == "C":
    print(f"The Temperature in Fahrenheit is: {round((temp*9)/5 + 32,2)}°F")
elif unit == "F":
    print(f"The Temperature in Celsius is: {round((temp - 32)*5/9, 2)}°C")
else:
    print(f"This {unit} is a invalid unit of measurement.")