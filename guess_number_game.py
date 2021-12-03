import random
import tkinter as tk

a = tk.Title('Number Guessing Game')

u = random.randint(1,100)

i = int(input("Guess the number: "))

while i != u:
    if i > u:
        print("You have entered a high number.")
        i = int(input("Guess again: "))
    elif i < u:
        print("You have entered a low number.")
        i = int(input("Guess again: "))
    elif i == u:
        print("You have entered correct choice.")
    
print("The number was", u)