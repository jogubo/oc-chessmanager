from os import system
from datetime import date


def clear():
    """Clear the terminal"""
    system('clear')


def prompt(message=None):
    """Custom prompt"""
    if message is not None:
        print(f"\n{message}")
    _input = input('>> ')
    return _input
