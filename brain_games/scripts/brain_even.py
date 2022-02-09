#!/usr/bin/env python
from brain_games.cli import welcome_user
from brain_games.games.even import play_even


def play():
    name = welcome_user()
    play_even(name)


def main():
    play()


if __name__ == '__main__':
    main()
