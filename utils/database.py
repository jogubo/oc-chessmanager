from tinydb import TinyDB


class Database:

    @staticmethod
    def table(table):
        db = TinyDB('db.json')
        table = db.table(table)
        return table

    @staticmethod
    def get(table):
        table = Database.table(table)
        table = table.all()
        return table

    @staticmethod
    def add(table, serialized):
        table = Database.table(table)
        table.insert_multiple(serialized)
