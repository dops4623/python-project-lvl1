#!/usr/bin/env python
from brain_games.cli import welcome_user
from brain_games.games.prime import play_prime


def play():
    name = welcome_user()
    play_prime(name)


def main():
    play()


if __name__ == '__main__':
    main()
