from os import system


def clear():
    """Clear the terminal"""
    system('clear')


def prompt(message=None):
    """Custom prompt"""
    if message is not None:
        print(message)
    _input = input('>> ')
    return _input
