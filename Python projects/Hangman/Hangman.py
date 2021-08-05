import random
from words import *
import string

def get_valid_word(words):

    word = random.choice(words) # randomly chooses some word from the list in Words.py
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    # word = get_valid_word(english) # chooses a word
    lib = input("Whitch kind of word library would you want to use? \n(english, czech, custom1, custom2, custom3) \n>>")
    print("\n")
    if lib == "english":
        word = get_valid_word(english)
    elif lib == "czech":
        word = get_valid_word(czech)
    elif lib == "custom1":
        word = get_valid_word(custom1)
    elif lib == "custom2":
        word = get_valid_word(custom2)
    elif lib == "custom3":
        word = get_valid_word(custom3)
    else:
        print("Invalid...")
        return

    word_letters = set(word) # letters in our word
    alphabet = set(string.ascii_uppercase) # letters in an alphabet
    used_letters = set() # Already guessed letters

    lives = 7
    

    while len(word_letters) > 0 and lives > 0:

        # displaying letters that has been already used
        print("You have", lives, "lives left and you have used these letters: ", " ".join(used_letters))

        # Displaying current word
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))

        # getting uset input
        used_letter = input("Guess a letter: ").upper()
        if used_letter in alphabet - used_letters:
            used_letters.add(used_letter)
            if used_letter in word_letters:
                word_letters.remove(used_letter)
                print(">> Correct!")

            else:
                lives -= 1
                print(">> Letter is not in the word.")

        elif used_letter in used_letters:
            print(">> You have already guessed that character. Please try again.")

        else:
            print(">> Invalid character. Please try again.")
        
        print("\n")

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print("You died, sorry. The word was", word)
    else:
        print("You guessed the word ", word, "correctly!")

while True:
    hangman()