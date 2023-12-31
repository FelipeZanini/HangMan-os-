""" This file contains the main functions of the hangman game """
# Import random module to select random words
import random
from words import WORDS_LIST
# Import hangman stages
from hangman import HANGMAN_STAGES


def get_word():
    """
    Get a random word from a list of words.
    """
    word = random.choice(WORDS_LIST).upper()
    return word


def play(word):
    """
    Responsible for getting the guesses from the user, and assures that
    only single letters or the whole word will be inputted, calling the
    function to display the hangman whether the player failed in his attempt
    or guessed the letter or the mystery word.
    """
    tries = 0
    right_guesses = []
    wrong_guesses = []
    display_hangman(word, right_guesses, tries)
    # Evaluate if the user run out of tries or guessed the word
    while len(word) != len(right_guesses) and tries != 6:
        guess = input("\n\nPlease, enter your guess: ").upper()
        # Break the loop if the user guessed the whole word
        if guess == word:
            return tries
        # Only accept one single letter as a input, otherwise will keep looping
        while not guess.isalpha() or len(guess) != 1:
            guess = input("Sorry invalid input, please try again: ").upper()
        # Assures that only new guesses are inputted
        if guess not in right_guesses and guess not in wrong_guesses:
            # Append the right guess to the list of right guesses
            right_guesses += [guess for char in word if char == guess]
            # Append the wrong guess to the list of wrong guesses
            if guess not in word:
                tries += 1
                wrong_guesses.append(guess)
        else:
            print(f"\nSorry, - {guess} - was already typed!")
            continue
        display_hangman(word, right_guesses, tries)
    return tries


def play_again(tries, word):
    """
    The game-over function is called whether the player
    runs out of tries or when the word is guessed,
    asking if the player would like to keep playing.
    """
    win_message = f"\nConsgratulations, the word is {word} \n"
    lose_message = f"\nSorry, You run out of guesses the word is {word} \n"
    # Print to the user whether he won or lost the game
    message = lose_message if tries == 6 else win_message
    print("\n---------------------------------------------------")
    print(message)
    print("---------------------------------------------------")
    # Will loop until the user, enters his intention to leave or stay playing
    while True:
        keep_playing = input("\nWould you like to keep playing? y/n ").upper()
        if keep_playing == "Y":
            print("\n-----------------")
            print("Hangman Game")
            print("-----------------\n")
            main()
        elif keep_playing == "N":
            print("\nLeaving the game...")
            return False
        else:
            print(f"\n- {keep_playing.upper()} - is not a valid option")


def display_hangman(word, guessed, tries):
    """
    Give visual feedback to the user, in which hangman stage he's,
    also, the words guessed so far.
    """
    print(HANGMAN_STAGES[tries])
    # Display the letter of the word, as an underscore,
    # or the letter itself whether the user guessed it
    mistery_word = [char if char in guessed else "_" for char in word]
    for char in mistery_word:
        print(char, end='  ')


def main():
    """
    Main function
    """
    word = get_word()
    tries = play(word)
    play_again(tries, word)


print("\n----------------------- \n")
print("welcome to Hangman Game")
print("\n----------------------- ")
main()
