list = [] #declaring empty array

while(True): #while loop for error checking and an option to terminate program when needed
    print("What would you like to do?") #printing options
    print("1. Add to list")
    print("2. Remove from list")
    print("3. View my list")
    print("4. Exit\n")

    choice = input('') #taking user input

    if(choice == '1'):
        item = input("What would you like to add?\n")
        list.append(item) #adding item to list
    elif(choice == '2'):
        item = input("What would you like to remove?\n")
        list.remove(item) #removing item from list
    elif(choice == '3'):
        print("Here is what you're missing! " + list) #printing list
    elif(choice == '4'):
        break #breaking out of loop and terminating program
    else:
        print("Please enter a valid option.") #ask to enter valid option if other option is chosen
    