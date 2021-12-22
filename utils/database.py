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
    def update(cls, table, key, value, doc_ids):
        table = cls.table(table)
        table.update({key: value}, doc_ids=doc_ids)

    @classmethod
    def search(cls, table, search):
        table = cls.table(table)
        q = Query()
        search = table.search(q.last_name == search)
        results = []
        for item in search:
            id = item.doc_id
            results.append(id)
            print(item, id)
            print(results)
        return results
