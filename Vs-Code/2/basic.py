# types of datatypes
# var1 = "GSoc 2026" #string datatypes
# var2 = 2026 #integer datatypes
# var3 = True #boolean datatypes
# var4 = 20.26 #float datatypes
# var5 = 24j #imaginary datatypes like complex number
# #etc.....

# #fstring
# print("There are too many conributors in the world who is better than you.")
# print(f"Types of datatypes: {var1} etc....")

# module importing
# import pyttsx3
# pyttsx3.speak("This is gonna be the first tutorial after a months or weeks")
# engine = pyttsx3.init()
# engine.say("I will let you know that you're a vampire")
# engine.runAndWait()

# engine = pyttsx3.init()
# engine.say("""Mariam said to Nana, "How are you Nana ?" """)
# engine.runAndWait()

# Type conversion of data types
# new_var1 = int(var2)
# print(new_var1)

# input function
# new_var2 = int(input("enter your age: "))
# if new_var2 > 100:
#     print("Are you a eternal being umm ? ")
# else: 
#     print(f"your age is:: {new_var2}")

#  if-elif-else treee
# new_usr = int(input("Enter your age: "))
# if new_usr > 100:
#     global iden
#     iden = "Eternal"
#     new_usr_co = str(input(f"Do you really think that you're {iden}?(y/n)" ))
#     if new_usr_co == "y":
#         print(f"How dare you think that.")
#         print("You're just an old man")
#     elif new_usr_co == "n":
#         print("then why do you entered age greater than 100")
#         print("don't you kow human can't live more than 80-100 years")
#     else:
#         print("You fool you can't even choose y/n")
# elif new_usr < 100:
#     print("you really think that you're a human being")
#     new_usr_2 = str(input("y/n"))
#     if new_usr_2 == "y":
#         print("who told you that you're human") 
#     elif new_usr_2 == "n":
#         print("what ??")
#     else:
#         print("you fool")
# else:
#     print("then what are you dude not a human or something else then what ?? ")

#dictionary
dict_2 = {"Rajeev":"idk", "Nandu":"Noobs","Vivek":"idk2","soon":"3rd","Sonu":"idk3",
 "Kishan":"Arunachal pradesh","Alok":"Tm_tanu","Anshu":"Next window","Sandeep":"classmate","Subham":"Single"}

usrp = input("ENTER YOUR NAME:: ")
print(f"{dict_2.get(usrp.capitalize(),"invalid input")}")