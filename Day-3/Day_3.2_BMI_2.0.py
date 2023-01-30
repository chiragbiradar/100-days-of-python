height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

BMI = float(weight)/(float(height)**2)

BMI = round(BMI)

print(f"Your BMI is {BMI}")

if BMI<18.5:
    print("You are under weight")
elif BMI<25:
    print("You are normal weight")
elif BMI<30:
    print("You are overweight")
elif BMI<35:
    print("You are obese")
else:
    print("You are clinically obese")
