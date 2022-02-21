import random

from brain_games.engine import play


def play_progression(name):
    print('What number is missing in the progression?')
    play(name, ask_question, correct_answer)


def ask_question():
    n = random.randint(5, 9)
    n1 = random.randint(0, 10)
    add = random.randint(1, 10)
    position = random.randint(2, n-1)
    res = str(n1)
    prev = n1
    for i in range(n):
        res += f' {prev+add}' if i+1 != position else ' ..'
        prev += add
    return res


def correct_answer(expression):
    a = expression.split(' ')
    if a[0] != '..' and a[1] != '..':
        add = int(a[1])-int(a[0])
    else:
        add = int(a[3])-int(a[4])
    i = a.index('..')
    res = int(a[i-1])+add
    return res
