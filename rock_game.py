#rock beats scissors
#scissors beats paper
#paper beats rock

import random
import time

options = ['rock', 'paper', 'scissors']

while(True):
    user_choice = input("Please chose an option! (rock, paper, scissors)\n")

    if(user_choice == 'rock' or user_choice == 'paper' or user_choice == 'scissors'):
        break
    else:
        print("Please chose a valid option!\n")

ai_choice = random.choice(options)

print('\n\nrock ')
time.sleep(1)
print('paper ')
time.sleep(1)
print('scissors!\n')
time.sleep(1)

print('You chose: ' + user_choice)
print('Ai chose: ' + ai_choice + '\n')

if(user_choice == ai_choice):
    print("It's a tie!")
elif(user_choice == 'rock'):
    if(ai_choice == 'paper'):
        print("Paper covers rock! Better luck next time.")
    else:
        print("Rock smashes scissors! You win!")
elif(user_choice == 'paper'):
    if(ai_choice == 'scissors'):
        print("Scissors slices paper! Better luck next time.")
    else:
        print("Paper covers rock! You win!")
elif(user_choice == 'scissors'):
    if(ai_choice == 'rock'):
        print("Rock smashes scissors! Better luck next time.")
    else:
        print("Scissors slices paper! You win!")