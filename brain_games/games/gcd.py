import math
import random

from brain_games.engine import play


def play_gcd(name):
    print('Find the greatest common divisor of given numbers.')
    play(name, ask_question, correct_answer)


def ask_question():
    n1 = random.randint(0, 100)
    n2 = random.randint(0, 100)
    return f'{n1} {n2}'


def correct_answer(expression):
    a, b = expression.split(' ')
    res = math.gcd(int(a), int(b))
    return res
