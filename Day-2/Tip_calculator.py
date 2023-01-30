print("Welcome to tip calculator")

total_bill = float(input("What was the total bill? $"))

tip_percent = ("what percent tip would you like to give? 10, 12 or 15?")

number_of_people = ("How many people to split the bill? ")

answer = (((total_bill*100)/tip_percent)/number_of_people)

print("Each person should pay: $" + answer)

#day 1