# dictionary to store user accounts
accounts = {
    "user1": {"password": "password1", "balance": 1000},
    "user2": {"password": "password2", "balance": 2000},
    "user3": {"password": "password3", "balance": 3000}
}

# function to log in to the account
def login():
    while True:
        username = input("Enter your username: ")
        if username in accounts:
            password = input("Enter your password: ")
            if password == accounts[username]["password"]:
                return username
            else:
                print("Incorrect password. Try again.")
        else:
            print("Username not found. Try again.")

# function to deposit money into the account
def deposit(username):
    amount = float(input("Enter the amount to deposit: "))
    accounts[username]["balance"] += amount
    print(f"Deposited {amount}. Current balance is {accounts[username]['balance']}.")

# function to withdraw money from the account
def withdraw(username):
    amount = float(input("Enter the amount to withdraw: "))
    if amount > accounts[username]["balance"]:
        print("Insufficient balance.")
    else:
        accounts[username]["balance"] -= amount
        print(f"Withdrew {amount}. Current balance is {accounts[username]['balance']}.")

# function to transfer money to another account
def transfer(username):
    recipient = input("Enter the recipient's username: ")
    if recipient in accounts:
        amount = float(input("Enter the amount to transfer: "))
        if amount > accounts[username]["balance"]:
            print("Insufficient balance.")
        else:
            accounts[username]["balance"] -= amount
            accounts[recipient]["balance"] += amount
            print(f"Transferred {amount} to {recipient}. Current balance is {accounts[username]['balance']}.")
    else:
        print("Recipient not found.")

# main program loop
while True:
    print("\nWelcome to the Bank Management System")
    print("------------------------------------")
    print("1. Login")
    print("2. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        username = login()
        while True:
            print("\nAccount Options")
            print("---------------")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Transfer")
            print("4. Logout")
            option = input("Enter your option: ")
            if option == "1":
                deposit(username)
            elif option == "2":
                withdraw(username)
            elif option == "3":
                transfer(username)
            elif option == "4":
                break
            else:
                print("Invalid option. Try again.")
    elif choice == "2":
        break
    else:
        print("Invalid choice. Try again.")