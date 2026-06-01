# Logical Operator = evaluate multiple condition (or, and , not)
#                   or - at least one condition must be true 
#                   and - both condition must be true
#                   not - invert the condition ( not true , not false)

# temp = 25
# is_raining = False
# if temp > 38 or temp < 0 or is_raining:
#     print('The outdoor event is cancelled')
# else:
#     print("The outdoor event is scheduled. ")

temp2 = 20
is_sunny = False
if temp2 >= 28 and is_sunny:
    print("It is HOT outside.")
elif temp2 <= 0 and is_sunny:
    print("It is cold outside")
elif 28 > temp2 > 0 and is_sunny:
    print("It is warm outside")
    print("It is sunny outside.")
elif 28 > temp2 > 0 and not is_sunny:
    print("It is cold outside")
    print("It is cloudy.")
