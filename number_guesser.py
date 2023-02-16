import random   #import module to use random function

number = random.randint(0,9)    #assigning number to a number between 1 and 10

while(True):    #while loop keeps running until we break out fo it
    guess = input("Please chose a number between 1 and 10\n")   #assigning guess variable to what the user inputs

    if(int(guess) < number):    #if guess is too low print too low
        print("Too low!\n")
    elif(int(guess) > number):  #if guess is too high print too high
        print("Too high!\n")
    else:   #else (so if guess = number) break out of while loop
        break

print("Congratulations! The number was " + str(number))     #print congratulations and concatenate number as string to output it as well


#the int(guess) and str(number) that we see on lines 8, 10 and 15 are to change the types of those 
#in these cases we are changing guess to an int and number to a string variable to what we need