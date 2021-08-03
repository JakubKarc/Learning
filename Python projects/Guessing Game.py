from math import *
import random


def guess(x):
    randomNum = random.randint(1, x)
    guess = 0
    while guess != randomNum:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < randomNum:
            print("Sorry, guess again. Too low.")
        elif guess > randomNum:
            print("Sorry, guess again. Too high.")

    print(f"Yay, congrats. You have guessed the number {randomNum} correctly.")


def compGuess(x):
    low = 1
    high = x
    feedback = " "
    while feedback != "C":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input (f"is {guess} too high (H), too low (L), or correct (C)?")
        if feedback == "H":
            high = guess - 1
        elif feedback == "L":
            low = guess + 1

    print(f"Yay! The computer correctly guessed number {guess}, correctly")


game = input("Do you want to guess the number (ME), or do you want the computer to guess your number (COMP)?")

if game == "ME":
    guess(int(input("In what range do you want to guess?")))

elif game == "COMP":
    compGuess(int(input("In what range will your number be?")))

else:
    print("False input!! Try again with (ME) or (COMP).")