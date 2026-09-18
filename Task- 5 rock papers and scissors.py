'''
#11/09/2026
#------------------------------------TASK-1-----------------------------------------------------------
import random

player1_score = 0
player2_score = 0

for i in range(10):

    print("\nGame", i + 1)

    player1 = input("Enter Rock, Paper or Scissors: ").lower().strip()
    player2 = random.choice(["rock", "paper", "scissors"])

    print("Player1:", player1)
    print("Player2:", player2)

    if player1 == player2:
        print("Tie")

    elif player1 == "rock" and player2 == "paper":
        print("Player2 won")
        player2_score += 1

    elif player1 == "paper" and player2 == "scissors":
        print("Player2 won")
        player2_score += 1

    elif player1 == "scissors" and player2 == "rock":
        print("Player2 won")
        player2_score += 1

    else:
        print("Player1 won")
        player1_score += 1


print("\nFinal Score")
print("Player1:", player1_score)
print("Player2:", player2_score)

if player1_score > player2_score:
    print("Player1 is the Winner")

elif player2_score > player1_score:
    print("Player2 is the Winner")

else:
    print("Match Tie")

#---------------------------------------TASK-2---------------------------------------------------
'''

import random

def rps():
    print("Rock Paper Scissors Game")
    player = input("Enter rock, paper or scissors: ").lower()

    computer = random.choice(["rock", "paper", "scissors"])

    print("Player:", player)
    print("Computer:", computer)

    if player == computer:
        print("Tie")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("Player won")
    else:
        print("Computer won")


def guessing_game():
    print("Number Guessing Game")

    number = random.randint(1, 10)

    for i in range(5):
        guess = int(input("Guess the number between 1 and 10: "))

        print("Your guessed number:", guess)

        if guess == number:
            print("Correct! You won")
            break

        elif guess > number:
            print("Your guess is greater than the number")

        else:
            print("Your guess is less than the number")

    else:
        print("You lost!")
        print("The correct number was:", number)



def study():
    print("Study time")
    print("Focus on your studies!")


choice = int(input("Enter your choice: 1-RPS, 2-Guessing Game, 3-Study: "))

if choice == 1:
    rps()

elif choice == 2:
    guessing_game()

elif choice == 3:
    study()

else:
    print("No choice")

