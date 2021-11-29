from tinydb import TinyDB, Query


class Database:

    @staticmethod
    def table(table):
        db = TinyDB('db.json')
        table = db.table(table)
        return table

    @staticmethod
    def get(table, id=None):
        id = id
        table = Database.table(table)
        if id is None:
            item = table.all()
        else:
            item = table.get(doc_id=id)
        return item

    @staticmethod
    def add(table, serialized):
        table = Database.table(table)
        table.insert_multiple(serialized)

    @staticmethod
    def search(table, search):
        table = Database.table(table)
        q = Query()
        search = table.search(q.last_name == search)
        results = []
        for item in search:
            item["id"] = item.doc_id
            results.append(item)
        return results
