import random

rating = [line.split() for line in open("rating.txt", "r").readlines()]
rating = {name: int(score) for name, score in rating}

name = input("Enter your name: ")
print("Hello, {}".format(name))

if name in rating:
    score = rating[name]
else:
    score = 0

versions = input()
if versions == "original":
    options = ["rock", "paper", "scissors"]
elif versions == "extended":
    options = ["rock", "gun", "lightning", "devil", "dragon", "water", "air", "paper", "sponge", "wolf", "tree", "human", "snake", "scissors", "fire"]
else:
    options = versions.split(",")

print("Okay, let's start")
user = input()

while user != "!exit":
    computer = random.choice(options)

    if user == computer:
        print("There is a draw ({})".format(computer))
        score += 50
    elif user in options and (options.index(user) - options.index(computer)) % len(options) > len(options) // 2:
        print("Sorry, but computer chose {}".format(computer))
    elif user in options and (options.index(user) - options.index(computer)) % len(options) <= len(options) // 2:
        print("Well done. Computer chose {} and failed".format(computer))
        score += 100
    elif user == "!rating":
        print("Your rating: {}".format(score))
    else:
        print("Invalid input")

    user = input()

print("Bye!")
