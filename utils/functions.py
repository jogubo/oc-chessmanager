from os import system
from tinydb import TinyDB


def players_db(serialized_players):
    db = TinyDB('db.json')
    players_table = db.table('players')
    players_table.truncate()
    players_table.insert(serialized_players)


def clear():
    """Clear the terminal"""
    system('clear')


def prompt(message=None):
    """Custom prompt"""
    if message is not None:
        print(message)
    _input = input('>> ')
    return _input
