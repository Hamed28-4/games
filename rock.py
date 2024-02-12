import random
list = ["rock", "paper", "scissors"]
pc = random.choice(list)
you = input("rock, paper or scissors: to stop press \'s\': ")


while True:
    if pc == "rock" and you == "scissors":
        print(f"PC {pc} and you {you}. PC won\n")
    elif pc == "paper" and you == "rock":
        print(f"PC {pc} and you {you}. PC won\n")
    elif pc == "scissors" and you == "paper":
        print(f"PC {pc} and you {you}. PC won\n")
    elif you == "s":
        break

    elif pc == "rock" and you == "paper":
        print(f"You {you} and pc {pc}. You won\n")
    elif pc == "paper" and you == "scissors":
        print(f"You {you} and pc {pc}. You won\n")
    elif pc == "scissors" and you == "rock":
        print(f"PC {pc} and you {you}. You won\n")


    else:
        print(f"PC {pc} and you {you}. Draw\n")
    
    if you == "s":
        break
    you = input("rock, paper or scissors: to stop press \'s\': ")
    pc = random.choice(list)