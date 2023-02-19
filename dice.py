import random

choice = input("Chose even or odd!\n") #taking user input

dice1 = random.randint(1,6)
print('Dice 1 rolled a ' + str(dice1)) #rolling dice 1 and printing result

dice2 = random.randint(1,6)
print('Dice 2 rolled a ' + str(dice2)) #rolling dice 2 and printing result

sum = dice1 + dice2
print('The total is ' + str(sum)) #getting sum of dice

result = sum % 2 #using modulus to check if sum is even or odd

if(result == 0): #if it is 0 then result is even
    result = 'even'
else:
    result = 'odd' #else its odd

if(choice == result): #if user input is same as result (both are even or odd) then they win
    print('You guessed right!')
else:
    print('Better luck next time!') #else they lose