import random

# Get a valid level
while True:
    level = input("Level: ")
    if level.isnumeric() and int(level) > 0:
        level = int(level)
        break

# Generate random number
n = random.randint(1, level)

# Guessing loop
while True:
    guess = input("Guess: ")

    if not guess.isnumeric():
        continue

    guess = int(guess)

    if guess <= 0:
        continue

    if guess > n:
        print("Too large!")
    elif guess < n:
        print("Too small!")
    else:
        print("Just right!")
        break
