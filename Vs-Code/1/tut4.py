#We're gonna make a simple program for assigning grades to students based on their marks
#first we will take the marks as input from the user
#there is system of grading in which we will assign grades from A to F based on the marks obtained
#Grade A >= 90 Grade B >= 80 grade c >= 70 grade d >= 60 grade f < 60
#there will be 5 subjects and we will calculate the average marks and then assign the grade based on their marks
#Let's start from here
print("\t \t Welcome to Grade Assignment System")
print("\t \t _________________________________")
print("\t \t Please enter your marks for the following subjects:")
print("\t \t _________________________________")
maths = float(input("\t \tMaths: "))
physics = float(input("\t \tPhysics: "))
chemistry = float(input("\t \tChemistry: "))
biology = float(input("\t \tBiology: "))
english = float(input("\t \tEnglish: "))
avg_marks = (maths + physics + chemistry + biology + english) / 5 
print("\t \t _________________________________")
print("\t \tYour average marks are: ", avg_marks)
if avg_marks >= 90:
    print("\t \tYour grade is: A")
elif(avg_marks >= 80):
    print("\t \tYour grade is: B")
elif(avg_marks >= 70):
    print("\t \tYour grade is: C")
elif(avg_marks >= 60):
    print("\t \tYour grade is: D")
else:
    print("\t \tYour grade is: F")
