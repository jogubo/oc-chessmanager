from tinydb import TinyDB, Query


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

    @staticmethod
    def search(table, search):
        table = Database.table(table)
        q = Query()
        result = table.search(q.last_name == search)
        return result
