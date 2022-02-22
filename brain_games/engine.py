import prompt

from brain_games.cli import welcome_user

NUMBER_OF_ROUNDS = 3


def start(game):
    name = welcome_user()
    game.show_desc()
    play(name, game.ask_question, game.correct_answer)


def play(name, ask_question, correct_answer):
    for i in range(NUMBER_OF_ROUNDS):
        question = ask_question()
        print(f'Question: {question}')
        ans = prompt.string('Your answer: ')
        correct = correct_answer(question)
        if ans != str(correct):
            print(
                f"'{ans}' is wrong answer ;(. Correct answer was '{correct}'."
            )
            print(f"Let's try again, {name}!")
            return
        else:
            print("Correct!")
    print(f"Congratulations, {name}!")
