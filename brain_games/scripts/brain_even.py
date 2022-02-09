#!/usr/bin/env python
import random
import prompt


def play():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    answers = ['yes', 'no']
    for i in range(3):
        n = random.randint(0, 100)
        print(f'Question: {n}')
        ans = prompt.string('Your answer: ')
        if (n % 2 == 0 and ans == 'no') or (n % 2 != 0 and ans == 'yes'):
            correct = [x for x in answers if x != ans][0]
            print(
                f"'{ans}' is wrong answer ;(. Correct answer was '{correct}'."
            )
            print(f"Let's try again, {name}!")
            return
        else:
            print("Correct!")
    print(f"Congratulations, {name}!")


def main():
    play()


if __name__ == '__main__':
    main()
