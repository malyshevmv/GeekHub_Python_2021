'''
7. Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!
'''
def calculator(num_1, num_2, operation):
    if operation == '+':
        return f'{num_1 + num_2}'
    elif operation == '-':
        return f'{num_1 - num_2}'
    elif operation == '*':
        return f'{num_1 * num_2}'
    elif operation == '/':
        return f'{num_1 / num_2}'
    else:
        return 'operation not found'

print(calculator(3, 4, '/'))