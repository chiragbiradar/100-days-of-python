import random

nameAsCSV = input("Give me everybody's name, ")
names = nameAsCSV.split(", ")

print(f"{names[random.randint(0,len(names)-1)]} is going to buy the meal today!")