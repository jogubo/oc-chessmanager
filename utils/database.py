from tinydb import TinyDB, Query


class Database:

    @staticmethod
    def table(table):
        db = TinyDB('db.json')
        table = db.table(table)
        return table

    @classmethod
    def get(cls, table, id=None):
        id = id
        table = cls.table(table)
        if id is None:
            item = table.all()
        else:
            item = table.get(doc_id=id)
        return item

    @classmethod
    def add(cls, table, serialized):
        table = cls.table(table)
        table.insert_multiple(serialized)

    @classmethod
    def search(cls, table, search):
        table = cls.table(table)
        q = Query()
        search = table.search(q.last_name == search)
        results = []
        for item in search:
            item["id"] = item.doc_id
            results.append(item)
        return results
