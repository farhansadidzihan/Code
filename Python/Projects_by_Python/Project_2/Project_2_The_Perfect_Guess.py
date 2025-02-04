# || "The Perfect Guess Game" - Using Random Module, Loops , Conditional Logic, Exception Handling & File Handling By Python ||

# Module for computer's guess 
import random
compGuess = random.randint(1, 100)
userGuess = None
attemps   = 0

# Under loop construction
while True:

    # Exeption Handling
    try:
        userGuess = int(input("Guess a number between  1 to 100:\n"))
        attemps += 1
        if userGuess == compGuess:
            print(f"Congratulations! You've find the correct number in {attemps} attemps.")
            break
        else:
            if userGuess > compGuess:
                print("You guessed it wrong! Enter a smaller number")
            else:
                print("You guessed it wrong! Enter a greater number")
    except Exception as e:
        print("Please, Enter a number!")

# Opening a file & reading what was the previous highscore & then, if guess attemps are less than previous then, saving this info in that file
with open("highscore.txt") as f:
    previousScore = int(f.read())
if previousScore > attemps:
    with open("highscore.txt", 'w') as f:
        f.write(str(attemps))
        print(f"You're create a new highscore of {attemps} attemps!")