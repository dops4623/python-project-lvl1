#!/usr/bin/env python
from brain_games.cli import welcome_user
from brain_games.games.calc import play_calc


def play():
    name = welcome_user()
    play_calc(name)


def main():
    play()


if __name__ == '__main__':
    main()
