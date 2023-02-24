import random

# list of words to choose from
words = ["apple", "banana", "cherry", "orange", "kiwi", "grape", "pear"]

# function to choose a random word
def choose_word(words):
    return random.choice(words)

# function to check if the letter is in the word
def check_letter(letter, word):
    return letter in word

# function to display the word with underscores for missing letters
def display_word(word, guesses):
    displayed_word = ""
    for letter in word:
        if letter in guesses:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

# main program loop
word = choose_word(words)
guesses = set()
incorrect_guesses = 0

while incorrect_guesses < 6:
    print(display_word(word, guesses))
    if set(word) == guesses:
        print("Congratulations, you guessed the word!")
        break
    letter = input("Enter a letter: ")
    if letter in guesses:
        print("You already guessed that letter. Try again.")
    elif check_letter(letter, word):
        guesses.add(letter)
        print("Correct!")
    else:
        incorrect_guesses += 1
        print(f"Incorrect. You have {6 - incorrect_guesses} guesses left.")
else:
    print(f"Sorry, you ran out of guesses. The word was {word}.")