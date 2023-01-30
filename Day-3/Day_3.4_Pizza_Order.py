print("Welcome to Python pizza deliveries!")
size = input("What size do you want? S, M or L ")
add_pepporoni = input("Do you want pepporoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

total_bill = 0

if size=='S':
    if add_pepporoni=='Y':
        if extra_cheese=='Y':
            total_bill = 18
        else:
            total_bill = 17
    else:
        if extra_cheese=='Y':
            total_bill = 16
        else:
            total_bill = 15
elif size=='M':
    if add_pepporoni=='Y':
        if extra_cheese=='Y':
            total_bill = 24
        else:
            total_bill = 23
    else:
        if extra_cheese=='Y':
            total_bill = 21
        else:
            total_bill = 20
else:
    if add_pepporoni=='Y':
        if extra_cheese=='Y':
            total_bill=29
        else:
            total_bill=28
    else:
        if extra_cheese=='Y':
            total_bill=26
        else:
            total_bill=25

print(f"Your final bill is ${total_bill}")

