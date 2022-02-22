import random


def show_desc():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def ask_question():
    n = random.randint(0, 100)
    return n


def correct_answer(expression):
    n = int(expression)
    if n == 1:
        return 'no'
    upper = int(n / 2) + 1
    for i in range(2, upper):
        print(i)
        if n % i == 0:
            return 'no'
    return 'yes'
