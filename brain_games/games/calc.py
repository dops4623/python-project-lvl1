import random

from brain_games.engine import play


def play_calc(name):
    print('What is the result of the expression?')
    play(name, ask_question, correct_answer)


def ask_question():
    n1 = random.randint(0, 100)
    n2 = random.randint(0, 100)
    operation = ['+', '-', '*'][random.randint(0, 2)]
    return f'{n1} {operation} {n2}'


def correct_answer(expression):
    return eval(expression)
