questions = (
    ["Which metal has the highest melting point?:  "],
    ("How many colour can human eye see ?: "),
    ["What is i²(iota^sq.)?: "],
    ("How many bones in human adult body?: "),
    ("In OSI model, Application layer present at?: ")
)
options = (("A. Helium B.Tungsten C. Platnium D. Zirconium"),
          ("A. 8 B. 4 C. 7 D. 2"),
          ("A. 1 B. -1 C. 3 D. 11"),
          ("A. 207 B. 206 C. 45 D. 208"),
          ("A. 7th Layer B. 1st layer C. 5th layer D. 4th layer"))
guesses = []
answers = ("B","C","B","B","A")
score = 0
usr_ans = []

for question in questions:
    for each_question in question:
        print(each_question,end="")
    print()
    for option in options:
        for opt in option:
            print(opt,end="")
        print()
        usr_inp = input("Select the option: ").upper()
