def add(num1, num2): #function takes 2 variables
    ans = int(num1) + int(num2) #converts the user input into ints to get the sum
    print(num1 + ' + ' + num2 + ' = ' + str(ans)) #prints the answer

def sub(num1, num2):
    ans = int(num1) - int(num2)
    print(num1 + ' - ' + num2 + ' = ' + str(ans))  

def mul(num1, num2):
    ans = int(num1) * int(num2)
    print(num1 + ' * ' + num2 + ' = ' + str(ans))

def div(num1, num2):
    ans = int(num1) / int(num2)
    print(num1 + ' / ' + num2 + ' = ' + str(ans))


while (True): #while loop is used for error checking
    num1 = input("Please input the first number\n") #taking user input for num1
    sign = input("Please input tye operation (+,-,*,/)\n") #taking user input for operator
    num2 = input("Please input the second number\n") #taking user input for num2

    if(num1.isdigit() and num2.isdigit() and (sign == '+' or sign == '-' or sign == '*' or sign == '/')): #checking that both numbers are ints and proper operator is used
        break #if true break out of loop
    else: #if false display error message and loop back to user input
        print('Please enter whole numbers and proper operators!') 

if(sign == "+"):
    add(num1, num2) #calls add function if sign is +
elif(sign == "-"):
    sub(num1, num2) #calls sub function if sign is -
elif(sign == "*"):
    mul(num1, num2) #calls mul function if sign is *
elif(sign == "/"):
    div(num1, num2) #calls div function if sign is /