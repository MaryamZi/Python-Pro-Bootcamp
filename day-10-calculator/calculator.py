print("Welcome to the calculator!")

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

first_num = float(input("What's the first number? "))
second_num = 0
continue_with_last_calc = False

while True:
    for symbol in operations:
        print(symbol)
    operation = input("Pick an operation: ")
    second_num = float(input("What's the second number? "))

    result = operations[operation](first_num, second_num)

    print(f"{first_num} {operation} {second_num} = {result}")

    continue_with_last_calc = input(
        f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower() == "y"

    if continue_with_last_calc:
        first_num = result
    else:
        first_num = int(input("What's the first number? "))
