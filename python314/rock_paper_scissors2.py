"""Module providing a sandbox to enter a number"""


import random


# rock paper scissors
Shapes = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
          """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
          """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

hands = ["rock", "paper", "scissors"]

player_choice = (int(input(
    'Please inter your choice as a number:"0 for rock", "1 for paper", "2 for scissors"\n')))
computer_choice = random.randint(0, 2)
if player_choice < 3 or player_choice > 0:
    print("----------------------------------")
    print(
        f"Computer chose {computer_choice} which is {hands[computer_choice]}")
    print(Shapes[computer_choice])

    print("----------------------------------")

    print(f"Your chose {player_choice} which is {hands[player_choice]}")
    print(Shapes[player_choice])

    print("----------------------------------")


if player_choice >= 3 or player_choice < 0:
    print("You picked the wrong number you lose")
elif player_choice == computer_choice:
    print("Draw")

elif player_choice == 0 and computer_choice == 2:
    print("You win")
elif player_choice == 2 and computer_choice == 0:
    print("You lose")
elif player_choice < computer_choice:
    print("You lose")
elif player_choice > computer_choice:
    print("You win")
else:
    print("Somthing went wrong")
