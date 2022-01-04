import os


def clear():
    """Clear the terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')


def prompt(message=None):
    """Custom prompt"""
    if message is not None:
        print(f"\n{message}")
    _input = input('>> ')
    return _input
