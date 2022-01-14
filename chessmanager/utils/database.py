from tinydb import TinyDB, Query


class Database:

    @staticmethod
    def table(table):
        """
        Select table.

            Parameters:
                table (str): table name

            Return: table
        """
        db = TinyDB('db.json')
        table = db.table(table)
        return table

    @classmethod
    def get(cls, table, id=None):
        """
        Get item.

            Parameters:
                table (str): table name
                id (int): item id

            Returns:
                item (dict)
        """
        id = id
        table = cls.table(table)
        if id is None:
            item = table.all()
        else:
            item = table.get(doc_id=id)
        return item

    @classmethod
    def add(cls, table, serialized):
        """
        Add item.

            Parameters:
                table (str): table name
                serialized (dict): item
        """
        table = cls.table(table)
        table.insert_multiple(serialized)

    @classmethod
    def update(cls, table, key, value, doc_ids):
        """
        Update items.

            Parameters:
                table (str): table name
                key (str)
                value (str, int, float, tuple, list, dict)
                doc_ids (int, list): id or list of id of items to be updated
        """
        if isinstance(doc_ids, (int, str)):
            doc_ids = [doc_ids]
        table = cls.table(table)
        table.update({key: value}, doc_ids=doc_ids)

    @classmethod
    def search(cls, table, search):
        """
        Search item.

            Parameters:
                table (str): table name
                search (str) name request

            Returns:
                results (list): id list
        """
        table = cls.table(table)
        q = Query()
        search = table.search(q.last_name == search)
        results = []
        for item in search:
            id = item.doc_id
            results.append(int(id))
        return results
