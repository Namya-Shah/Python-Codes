# USER HAVE TO MAKE THE GUESS!!!

import random
from re import I
number = random.randrange(1,100)
guess = int(input("Guess a number between 1 and 100: "))

while guess != number:
    if guess < number:
        print("You need to guess higher. Try Again!")
        guess = int(input("\nGuess a number between 1 and 100: "))
    elif guess > number:
        print("You need to guess lower. Try again")
        guess = int(input("\nGuess a number between 1 and 100: "))
print("You did it!")