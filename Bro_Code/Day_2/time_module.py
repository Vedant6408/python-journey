import time

# time.sleep(4)
# print("Times Up !")

usr_time = int(input("Enter the time in second: "))
# for i in reversed(range(0,usr_time)):
for i in range(usr_time,0,-1):
    # time.sleep(usr_time)
    time.sleep(usr_time) #there is no difference after swaping line 9 to 10 
    print(i)
print("Time's UP!")