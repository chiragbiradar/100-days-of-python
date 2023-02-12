import random

print("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors.")
ans = int(input())

Rock = "🪨"
Paper = "🧻"
Scissor = "✂️"

data = [Rock, Paper, Scissor]

rand_opt = random.randint(0,2)

print(data[ans])
print(f"Computer chose:\n{data[rand_opt]}")

if ans==rand_opt:
    print("Draw")
elif (ans==0 and rand_opt==1):
    print("You lose")
elif (ans==0 and rand_opt==2):
    print("You won")
elif (ans==1 and rand_opt==0):
    print("You won")
elif (ans==1 and rand_opt==2):
    print("You lose")
elif (ans==2 and rand_opt==0):
    print("You lose")
elif (ans==2 and rand_opt==1):
    print("You Won")
else:
    print("Invalid input")