import random


def show_desc():
    print('What is the result of the expression?')


def ask_question():
    n1 = random.randint(0, 100)
    n2 = random.randint(0, 100)
    operation = ['+', '-', '*'][random.randint(0, 2)]
    return f'{n1} {operation} {n2}'


def correct_answer(expression):
    return eval(expression)
