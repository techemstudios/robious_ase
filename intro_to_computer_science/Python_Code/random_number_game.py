"""
A random number guessing game.
"""

import random
number = random.randint(1, 100)

print("I'm thinking of a number between 1-100")

GameRunning = True
while True:
    
    guess = int(raw_input("Guess a number between 1-100: "))

    if guess > number:
        print("Your guess is too high!")
    elif  guess < number:
        print("Your guess is too low!")
    elif guess == number:
        print("You guessed correctly!")
        GameRunning = False
        raw_input("\n\nPress enter key to exit ")
        exit()
 
