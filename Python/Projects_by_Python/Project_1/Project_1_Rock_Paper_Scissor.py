# || "Rock Paper Scissor Game" - Using Random Module, Loops & Conditional Logic By Python ||

# Module for generating random number
import random

while True:

    # Player's Turn
    player = input("Player's Turn: rock, paper or scissor?\n:-")

    # Conputer's Turn
    rand_num = random.randint(1, 3)
    if rand_num == 1:
        computer = 'rock'
    elif rand_num == 2:
        computer = 'paper'
    elif rand_num == 3:
        computer = 'scissor'
    print("Computer's Turn: rock, paper or scissor?\n:-", computer)

    # Logic for game
    if computer == 'rock' and player == 'paper':
        match = player
    elif computer == 'paper' and player == 'scissor':
        match = player
    elif computer == 'scissor' and player == 'rock':
        match = player
    elif computer == 'scissor' and player == 'scissor':
        match = None
    elif computer == 'rock' and player == 'rock':
        match = None
    elif computer == 'paper' and player == 'paper':
        match = None
    else:
        match = computer

    # Logic for statements
    if match == computer:
        print("You lose, Computer Win!")
    elif match == player:
        print("Congratulations! You Win!")
    else:
        print("The Match is Tie!")