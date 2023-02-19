import secrets
import string

letters = string.ascii_letters #assigning letters to be all upper and lower case letters
digits = string.digits #assigning digits to be numbers 0 to 9
special_chars = string.punctuation #assigning special_chars to be symbols

alphabet = letters + digits + special_chars #adding all the letters, numbers and characters in one place

pass_length = int(input("What should be the password length?\n")) #getting user input on how long password should be

password = '' #initializing password string to nothing

for i in range(pass_length):
    password += ''.join(secrets.choice(alphabet)) #for loop to add a random letter, number of symbol into our password until password length is reached

print("Here is your new password!\n" + password) #printing password