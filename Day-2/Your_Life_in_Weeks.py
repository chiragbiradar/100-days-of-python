age = input("What is your current age? ")

age = int(age)

years_ream = 90 - age
days_rem = years_ream * 365
weeks_rem = years_ream* 52
months_rem = years_ream * 12

print(f"You have {days_rem} days, {weeks_rem} weeks and {months_rem} months left")