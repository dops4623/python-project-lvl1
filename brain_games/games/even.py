import random

from brain_games.engine import play


def play_even(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    play(name, ask_question, correct_answer)


def ask_question():
    return random.randint(0, 100)


def correct_answer(expression):
    answer = 'yes' if int(expression) % 2 == 0 else 'no'
    return answer
