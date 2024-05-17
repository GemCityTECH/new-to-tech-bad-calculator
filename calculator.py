# my_first_calculator.py by AceLewis
# TODO: Make it work for all floating point numbers too

if 3/2 == 1:  # Because Python 2 does not know maths
    input = raw_input  # Python 2 compatibility

print('Welcome to this calculator!')
print('It can add, subtract, multiply and divide whole numbers from 0 to 50')
num1 = int(input('Please choose your first number: '))
sign = input('What do you want to do? +, -, /, or *: ')
num2 = int(input('Please choose your second number: '))

def display(num1, sign, num2, answer):
    print(f"{num1} {sign} {num2} = {answer}")

def add_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(num1, num2):
    return num1 - num2

def multiply_numbers(num1, num2):
    return num1 * num2

def divide_numbers(num1, num2):
    return num1 / num2

def select_operation(num1, sign, num2):
    match sign:
        case "/":
            return divide_numbers(num1, num2)
        case "*":
            return multiply_numbers(num1, num2)
        case "+":
            return add_numbers(num1, num2)
        case "-":
            return subtract_numbers(num1, num2)
        case _:
            print(f"Operatore not recognized: {sign}")

answer = select_operation(num1, sign, num2)
display(num1, sign, num2, answer)

print("Thanks for using this calculator, goodbye :)")
