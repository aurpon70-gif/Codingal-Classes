import random

while True:
    user_action = input("Enter a choice (Rock, Paper, or Scissors):")
    possible_actions = ["rock", "paper", "scissors"]

    computer_action = random.choice(possible_actions)
    print(f"\nYou Chose {user_action}, and the computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"We both chose {user_action}. A Tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock Jams Scissors! You Win!")
        else:
            print("Paper Covers Rock! You Lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers Rock! You Win!")
        else:
            print("Scissors Cuts Paper! You Lose.")
    elif user_action == "scissors":
        if computer_action == "rock":
            print("Rock Jams Scissors! You Lose.")
        else:
            print("Scissors Cuts Paper! You Win!")
    play_again = input("Play again? (y/n): ")
    if play_again != "y":
        break

    