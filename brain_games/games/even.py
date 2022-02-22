import random


def show_desc():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def ask_question():
    return random.randint(0, 100)


def correct_answer(expression):
    answer = 'yes' if int(expression) % 2 == 0 else 'no'
    return answer
