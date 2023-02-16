def add(num1, num2):
    ans = int(num1) + int(num2)
    print(num1 + ' + ' + num2 + ' = ' + str(ans))

def sub(num1, num2):
    ans = int(num1) - int(num2)
    print(num1 + ' - ' + num2 + ' = ' + str(ans))  

def mul(num1, num2):
    ans = int(num1) * int(num2)
    print(num1 + ' * ' + num2 + ' = ' + str(ans))

def div(num1, num2):
    ans = int(num1) / int(num2)
    print(num1 + ' / ' + num2 + ' = ' + str(ans))

if (__name__ == '__main__'): #TODO: ADD ERROR CHECKING
    num1 = input("Please input the first number\n")
    sign = input("Please input tye operation (+,-,*,/)\n")
    num2 = input("Please input the second number\n")

    if(sign == "+"):
        add(num1, num2)
    elif(sign == "-"):
        sub(num1, num2)
    elif(sign == "*"):
        mul(num1, num2)
    elif(sign == "/"):
        div(num1, num2)