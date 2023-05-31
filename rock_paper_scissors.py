import random

user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")

try:
    with open("rating.txt", "r") as file:
        user_rating = 0
        for line in file:
            name, rating = line.strip().split()
            if name == user_name:
                user_rating = int(rating)
                break
except FileNotFoundError:
    user_rating = 0

print(f"Your rating: {user_rating}")

options = ["rock", "paper", "scissors", "gun", "lightning", "devil", "dragon", "water", "air", "sponge", "wolf", "tree", "human", "snake", "fire"]

beats = {
    "rock": ["scissors", "tree", "fire", "snake", "human"],
    "paper": ["rock", "air", "water", "dragon"],
    "scissors": ["paper", "sponge", "air", "tree", "human"],
    "gun": ["wolf", "tree", "sponge", "paper", "air", "water", "dragon", "devil", "dragon"],
    "lightning": ["tree", "human", "dragon", "sponge", "wolf", "scissors", "snake"],
    "devil": ["scissors", "snake", "human", "tree", "fire"],
    "dragon": ["snake", "human", "tree", "fire", "scissors", "snake", "sponge", "wolf"],
    "water": ["fire", "rock", "scissors", "snake", "human", "dragon"],
    "air": ["water", "dragon", "devil", "fire", "rock", "scissors"],
    "sponge": ["paper", "air", "water", "dragon", "devil", "dragon"],
    "wolf": ["tree", "human", "snake", "scissors", "sponge", "paper", "air", "water", "dragon", "devil", "dragon"],
    "tree": ["water", "dragon", "devil", "fire", "rock", "scissors", "snake"],
    "human": ["devil", "dragon", "snake", "scissors", "sponge", "paper"],
    "snake": ["scissors", "sponge", "air", "water", "dragon", "devil", "dragon"],
    "fire": ["tree", "human", "snake", "scissors", "sponge", "paper"]
}

while True:
    user_input = input()

    if user_input == "!exit":
        print("Bye!")
        break

    if user_input == "!rating":
        print(f"Your rating: {user_rating}")
        continue

    if user_input not in options and user_input != "":
        print("Invalid input")
        continue

    computer_choice = random.choice(options)

    if user_input == computer_choice:
        print(f"There is a draw ({computer_choice})")
        user_rating += 50
    elif computer_choice in beats[user_input]:
        print(f"Well done. The computer chose {computer_choice} and failed")
        user_rating += 100
    else:
        print(f"Sorry, but the computer chose {computer_choice}")

print("Game over!")

with open("rating.txt", "r+") as file:
    lines = file.readlines()
    file.seek(0)
    for line in lines:
        name, rating = line.strip().split()
        if name == user_name:
            rating = str(user_rating)
        file.write(f"{name} {rating}\n")
    file.truncate()