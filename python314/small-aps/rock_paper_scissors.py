"""Module providing a sandbox to enter a text"""

import random

# inp = input("inter your choice. ")

# striped = inp.strip()

# lower = striped.lower()

# choice = lower(strip(inp))

WINNER = ""

player_choice = (
    input('Please inter your choice:"rock", "paper", "scissors"\n')).strip().lower()
computer_choice = random.choice(["rock", "paper", "scissors"])
print(f"You chose: {player_choice}")
print(f"Computer chose: {computer_choice}")

if player_choice == computer_choice:
    print(f"Drow both selected: {player_choice}")

elif player_choice == "rock":
    if computer_choice == "paper":  # com=pap
        WINNER = "computer"
    elif computer_choice == "scissors":  # com=sci
        WINNER = "player"

elif player_choice == "paper":
    if computer_choice == "rock":  # com=rock
        WINNER = "player"
    elif computer_choice == "scissors":  # com=sci
        WINNER = "computer"

elif player_choice == "scissors":
    if computer_choice == "paper":  # com=pap
        WINNER = "player"
    elif computer_choice == "rock":  # com=rock
        WINNER = "computer"


if WINNER == "":
    print('You didn\'t choice "rock", "paper", "scissors"\n "GAME OVER"')
else:
    print(f"the winner is {WINNER}")
