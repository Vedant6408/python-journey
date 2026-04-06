import pyttsx3
# # string = "This is a string"
# # print(string[0:6])
# # a = 4.50
# # b = 4.75
# # print(type(a))
# # print(round(a))
# # print(round(b))
# # print(oct(23) + oct(23))
# # print(~2)
# #we're gonna concatenate two strings
# strn1 = "Mechanical"
# strn2 = "Keyboard"
# #using + operator to concatenate these two strings
# addedstr = strn1 + " " + strn2
# print(addedstr)
# print(len(addedstr))
# print(addedstr[0:12])
# def kishan():
#     print("This is a function")
# kishan() #this is how we call the function
# str3 = "Abdul kalam"
# print(str3[0:len(str3)]) #This is how we can print the whole string using string slicing
# #if we want to print the one letter from any string then we can do it like thiss
# print(str3[4])
# """
# This will print the letter 'l' from the string "Abdul kalam" because 
#   the index of 'l' is 4 in the string. 
#   """
# #This is how we use multiline comment in python
# #WE can also use negative indexing in python to access the characters from the end of the string\
# print(str3[-3])
# #In negative indexing, the index starts from -1 instead of 0, so the last character of the string has an index of -1

# #There are many function for strings in python, some of them are:
# print(str3.endswith("m"))
# print(strn1.startswith("N"))
# print(strn2.startswith("k")) #it means that the string "Keyboard" starts with the letter "k" not with K
# print(strn1.replace("a","2"))
# print(strn1.find("a"))

#1.WAP to input a string from user and print its length

# inp1 = input("Enter a string:")
# print("Length of the string is:", len(inp1))
# engine = pyttsx3.init()
# engine.say("lenght of the string is " + str(len(inp1)))
# engine.runAndWait()

# #2.WAP to print the occurence of a letter in a string
# occstr = "Universe if infinite and so is our curiosity"
# print(occstr.count("e")) #it will count the number of times the letter "e" occurs in the string

text = "Banana"
text.upper()
text.replace("a", "o")
print(text)