print("Welcome to love calculator!")
name1=input("What is your name?\n")
name2=input("What is their name?\n")

name1=name1.lower()
name2 = name2.lower()

true_count = name1.count("t")+name1.count("r")+name1.count("u")+name1.count("e")+name2.count("t")+name2.count("r")+name2.count("u")+name2.count("e")

love_count = name1.count("l")+name1.count("o")+name1.count("v")+name1.count("e")+name2.count("l")+name2.count("v")+name2.count("o")+name2.count("e")

result = true_count*10+love_count

if (result<10 or result>90):
    print(f"Your Love score is {result}%, you go together like coke and mentos.")
elif (result>40 and result<50):
    print(f"Your score is {result}%, you are alright together.")
else:
    print(f"Your score is {result}%.")