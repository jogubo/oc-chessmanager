from os import system
from tinydb import TinyDB


def open_db(table):
    db = TinyDB('db.json')
    table = db.table(table)
    table = table.all()
    return table


def save_db(table, serialized):
    db = TinyDB('db.json')
    table = db.table(table)
    table.truncate()
    table.insert_multiple(serialized)


def clear():
    """Clear the terminal"""
    system('clear')


def prompt(message=None):
    """Custom prompt"""
    if message is not None:
        print(message)
    _input = input('>> ')
    return _input
