import random
number = int(input("Enter a number between 1 to 99: "))
guess = random.randint(1, 99)
print(f"My guess is {guess}")

print("Enter 'm' if the number > guess, 'l' if number < guess, 't' if number == guess.")

hint = input("Enter your command: ")

while hint != "t":
    if hint == "l":
        while hint != "t":
            if hint == "l":
                guess = random.randint(1, guess)
                print(f"My guess is {guess}")
                hint = input("Enter your command: ")
            elif hint == "m":
                guess = random.randint(guess, number)
                print(f"My guess is {guess}")
                hint = input("Enter your command: ")

    elif hint == "m":
        while hint != "t":
            if hint == "m":
                guess = random.randint(guess, 99)
                print(f"My guess is {guess}")
                hint = input("Enter your command: ")
            elif hint == "l":
                guess = random.randint(number, guess)
                print(guess)
                print(f"My guess is {guess}")
                hint = input("Enter your command: ")

print('Wow, I guessed the number correctly!!')