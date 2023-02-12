print("Welcome to tip calculator")

total_bill = float(input("What was the total bill? $"))

tip_percent = float(input("what percent tip would you like to give? 10, 12 or 15?"))

number_of_people = int(input("How many people to split the bill? "))

answer = ((total_bill*tip_percent)/100)
answer = (total_bill+answer)/number_of_people
answer=round(answer,2)

print(f"Each person should pay: $ {answer}")

#Tip calculator
