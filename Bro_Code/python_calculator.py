#python calculator
operator = input("Enter an Operator (+ - * /): ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
# if operator == "+":
#     print(f"The sum of two number is: {num1+num2}")
# elif operator == "-":
#     print(f"The difference btw them is: {num1-num2}")
# elif operator == "*":
#     print(f"The product of these two number is: {num1*num2}")
# elif operator == "/":
#     print(f"Quotient will be: {int(num1/num2)}")
# else: 
#     print("Syntax Error")

#We can create this conditional statement in difference method like this 
if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2 
    print(result)
elif operator == "/":
    result = num1 / num2 
else:
    print(f"This {operator} is not a valid operator")
#in this statement there is a variable called result which will be updated after every line if the condition is true
#if the condition is not true then that variable stuck there and through out the result on that condition