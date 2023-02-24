import random

# define the flashcards as a dictionary
flashcards = {
    "What is the capital of France?": "Paris",
    "What is the highest mountain in the world?": "Mount Everest",
    "What is the largest country in the world by land area?": "Russia",
    "What is the currency of Japan?": "Yen",
    "What is the name of the longest river in Africa?": "Nile",
    "What is the name of the largest desert in the world?": "Sahara"
}

# function to display a random flashcard
def display_flashcard():
    question = random.choice(list(flashcards.keys())) # choose a random question from the flashcards
    print(question) # display the question
    answer = input("Enter your answer: ") # ask the user for their answer
    if answer.lower() == flashcards[question].lower(): # check if the answer is correct
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {flashcards[question]}.")

# main program loop
while True:
    choice = input("Press enter to display a flashcard, or type 'q' to quit: ")
    if choice.lower() == "q":
        break
    display_flashcard()