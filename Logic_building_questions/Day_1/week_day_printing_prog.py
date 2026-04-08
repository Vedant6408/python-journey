#weekdays printing program without any module
num_of_days_in_weeks = 7
print("How many weeksdays you wanna calculate ? ")
usr_inp = input("Enter no. of weeks? :: ")
if usr_inp.isdigit():
    usr_inp = int(usr_inp)
    print(f"The number of day in {usr_inp} weeks is : {usr_inp*7} days.")
else:
    print("invalid input")
    print("there is only integer value acceptable")