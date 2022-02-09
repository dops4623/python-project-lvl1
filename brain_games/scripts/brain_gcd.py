#!/usr/bin/env python
from brain_games.cli import welcome_user
from brain_games.games.gcd import play_gcd


def play():
    name = welcome_user()
    play_gcd(name)


def main():
    play()


if __name__ == '__main__':
    main()
