#!/usr/bin/env python
from brain_games.cli import welcome_user
from brain_games.games.progression import play_progression


def play():
    name = welcome_user()
    play_progression(name)


def main():
    play()


if __name__ == '__main__':
    main()
