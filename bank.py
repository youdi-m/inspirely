class NewUser(object):
    name = ""
    password = ""
    balance = 0

    def __init__(self, name, password, balance):
        self.name = name
        self.password = password
        self.amount = balance

def new_user(name, password, balance):
    user = NewUser(name, password, balance)
    return NewUser

while(True):
    
    print("Welcome to Inspirely Bank! What would you like to do?\n")
    print("[1] Sign Up")
    print("[2] Deposit")
    print("[3] Withdraw")
    print("[4] Exit")

    choice = input("")

    if(choice == '1'):
        print()
    elif(choice == '2'):
        print()
    elif(choice == '3'):
        print()
    elif(choice == '4'):
        print()
    else:
        print()