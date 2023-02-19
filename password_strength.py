import string

letters = string.ascii_letters #assigning letters to be all upper and lower case letters
digits = string.digits #assigning digits to be numbers 0 to 9
special_chars = string.punctuation #assigning special_chars to be symbols

password_strength = 0 #initializing password strength to 0
password = input("Please enter your password.\n") #getting user input for password

lower = sum(c.islower() for c in password)
upper = sum(c.isupper() for c in password)
digit = sum(c.isdigit() for c in password)
char = sum(c.isalnum() for c in password)

if(int(lower) + int(upper) >= 6):
    password_strength += 1
elif(int(lower) + int(upper) >= 8):
    password_strength += 2
elif(int(lower) + int(upper) >= 10):
    password_strength += 3

if(int(upper) > 1):
    password_strength += 1
elif(int(upper) >= 2):
    password_strength += 2

if(int(digits) >= 1):
    password_strength += 1
elif(int(digits) >= 2):
    password_strength += 2

if(int(char) >= 1):
    password_strength += 2
elif(int(char) >= 2):
    password_strength += 3

print("Your password strength is a " + str(password_strength) + "/5")