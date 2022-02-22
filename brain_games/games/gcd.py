import math
import random


def show_desc():
    print('Find the greatest common divisor of given numbers.')


def ask_question():
    n1 = random.randint(0, 100)
    n2 = random.randint(0, 100)
    return f'{n1} {n2}'


def correct_answer(expression):
    a, b = expression.split(' ')
    res = math.gcd(int(a), int(b))
    return res
