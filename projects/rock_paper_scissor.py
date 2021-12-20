import random

user_action = input("Enter your choice (Rock/Paper/Scissor): ")

possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, Computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("You Win!")
    else:
        print("You Lose!")
elif user_action == "paper":
    if computer_action == "scissors":
        print("You Win!")
    else:
        print("You Lose!")
elif user_action == "scissors":
    if computer_action == "paper":
        print("You Lose!")
    else:
        print("You Win!")
else:
    print("You have entered wrong choice.")