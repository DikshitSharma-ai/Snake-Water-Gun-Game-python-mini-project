# Snake Water Gun Game
# Mini Python Project (Loops + Conditions)
# Author: Dikshit Sharma


import random

# -----------------------------
# Game Setup
# -----------------------------

choices = ["snake", "water", "gun"]
user_score = 0
computer_score = 0


# -----------------------------
# Game Loop (5 Rounds)
# -----------------------------

for i in range(5):

    user = input("Enter your choice: ").lower()
    print("\nYou chose: ", user)

    computer = random.choice(choices)
    print("Computer chose: ", computer)


    # -----------------------------
    # Game Logic
    # -----------------------------

    if user == computer:
        print("Draw")

    elif(
        (user == "snake" and computer == "water") or
        (user == "water" and computer == "gun") or
        (user == "gun" and computer == "snake")
    ):
        print("You win")
        user_score += 1

    elif user in choices:
        print("Computer wins")
        computer_score += 1

    else:
        print("Wrong input")


# -----------------------------
# Final Result
# -----------------------------

print("\nFinal score: ")
print("You", user_score)
print("Computer", computer_score)