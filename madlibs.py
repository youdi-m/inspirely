print("Welcome to the Madlibs Story Teller!")
print("-----------------------------------")

# ask for input from user
name = input("Enter a name: ")
noun1 = input("Enter a noun: ")
verb1 = input("Enter a verb: ")
adjective1 = input("Enter an adjective: ")
noun2 = input("Enter another noun: ")
verb2 = input("Enter another verb: ")
adjective2 = input("Enter another adjective: ")
verb3 = input("Enter one more verb: ")

# display the story with user inputs
print(f"Once upon a time, there was a person named {name}.")
print(f"{name} loved {noun1}, and often spent time {verb1} with {noun1}.")
print(f"{name} was known for being {adjective1}, and people often asked {name} to help with {noun2} because of this.")
print(f"One day, while {verb2}, {name} stumbled upon a {adjective2} {noun2}.")
print(f"{name} decided to {verb3} the {noun2} and it turned out to be a great success!")
print("The end.")