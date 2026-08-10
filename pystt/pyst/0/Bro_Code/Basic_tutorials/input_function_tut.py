#input function tutorial
# inp1 = input("Enter your name: ")
# print(f"Your name is {inp1}")
# #input function always return data in string datatype

# name = input("What is your name?: ")
# print(f"Hello {name} !")


#Exercise 1 Calc the ares of rectangle
# user_inp1 = int(input("Enter the lenght of a rectangle?: "))
# user_inp2 = int(input("Enter the breath of a rectangle? "))
# area = user_inp1*user_inp2
# print(f"The Area of a rectangle is: {area} cm²")


#Exercise 2 Making a shoping cart program

item = input("What would you like to buy?: ")
price = float(input("How much the cost of that item?: "))
quantity = int(input("How many you wanna buy?: "))
total = price * quantity
print(f"You bought {item} and the total price is: ${total} ")