# Simple Python Calculator
def simple_calculator(a, b, operation):
    if operation == "+":
        print(f'{a} {operation} {b} = {a + b}') 
    elif operation == "-":
        print(f'{a} {operation} {b} = {a - b}')
    elif operation == "*":
        print(f'{a} {operation} {b} = {a * b}')
    elif operation == "/":
        print(f'{a} {operation} {b} = {a / b}')
    else:
        print("Invalid operation")
    
#Example usage
simple_calculator(5, 10, "+")
simple_calculator(11, 3, "-")
simple_calculator(7, 9, "*")
simple_calculator(12, 4, "/")
simple_calculator(12, 4, "%")