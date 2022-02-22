import prompt


def play(name, ask_question, correct_answer):
    for i in range(3):
        expression = ask_question()
        print(f'Question: {expression}')
        ans = prompt.string('Your answer: ')
        correct = correct_answer(expression)
        if ans != str(correct):
            print(
                f"'{ans}' is wrong answer ;(. Correct answer was '{correct}'."
            )
            print(f"Let's try again, {name}!")
            return
        else:
            print("Correct!")
    print(f"Congratulations, {name}!")
