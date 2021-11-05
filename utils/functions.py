from os import system


def clear():
    system('clear')


def prompt(message=None):
    if message is not None:
        print(message)
    _input = input('>> ')
    return _input
