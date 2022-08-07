from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2



operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide 
}



def calculator():

    print(logo)
    calc_next = 'y'
    num1 = float(input("What's the first number?: "))

    while calc_next == 'y':

        num2 = float(input("What's the second number?: "))

        for operator in operations:
            print(operator)

        operation_symbol = input("Pick an operation from the lines above: ")
        output = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {output}")
        calc_next = input(f"type 'y' to continue calculating with {output} or type 'n' for new calculation: ")
        num1 = output
    
    calculator()


calculator()