# my_first_calculator.py by AceLewis
# TODO: Make it work for all floating point numbers too

if 3/2 == 1:  # Because Python 2 does not know maths
    input = raw_input  # Python 2 compatibility

print('Welcome to this calculator!')
print('It can add, subtract, multiply and divide whole numbers from 0 to 50')
num1 = int(input('Please choose your first number: '))
sign = input('What do you want to do? +, -, /, or *: ')
num2 = int(input('Please choose your second number: '))

def addNums(num1, num2):
    print(f"{num1} + {num2} = {num1 + num2}")

def subNums(num1, num2):
    print(f"{num1} - {num2} = {num1 - num2}")

def division_multi(num1,sign,num2):
    if sign == "/":
        print(f"{num1} {sign} {num2} = {num1 / num2}")
    elif sign == "*":
       print(f"{num1} {sign} {num2} = {num1 * num2}")
    else:
        print("This operation did not include * or /")

def display(num1, num2, sign, answer):
    print(f"{num1} {sign} {num2} = {answer}")

if (sign == '+'):
    answer = addNums(num1, num2)
elif (sign == '-'):
    answer = subNums(num1, num2)

division_multi(num1,sign,num2)

print("Thanks for using this calculator, goodbye :)")