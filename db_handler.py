import threading
from tinydb import Query, where


class DbHandler:
    instance = None

    @staticmethod
    def get_instance():
        if DbHandler.instance is None:
            DbHandler.instance = DbHandler()

        return DbHandler.instance

    def __init__(self):
        self.lock = threading.Lock()

    def read_all(self, db):
        transaction = {'db': db, 'operation': 'read_all'}
        return self._handle_transaction(transaction)

    def read(self, db, id):
        transaction = {'db': db, 'id': id, 'operation': 'read'}
        return self._handle_transaction(transaction)

    def contains(self, db, id):
        transaction = {'db': db, 'id': id, 'operation': 'contains'}
        return self._handle_transaction(transaction)

    def write(self, db, record):
        transaction = {'db': db, 'record': record, 'operation': 'write'}
        self._handle_transaction(transaction)
        return

    def update(self, db, id, record):
        transaction = {'db': db, 'id': id, 'record': record, 'operation': 'update'}
        self._handle_transaction(transaction)
        return

    def delete(self, db, id):
        transaction = {'db': db, 'id': id, 'operation': 'delete'}
        self._handle_transaction(transaction)
        return

    def _handle_transaction(self, transaction):
        operation = transaction['operation']

        with self.lock:
            if operation == 'read_all':
                db = transaction['db']
                return db.all()

            elif operation == 'read':
                db = transaction['db']
                id = transaction['id']
                return db.get(Query().id == id)

            elif operation == 'contains':
                db = transaction['db']
                id = transaction['id']
                return db.contains(where('id') == id)

            elif operation == 'write':
                db = transaction['db']
                record = transaction['record']
                db.insert(record)
                return

            elif operation == 'update':
                db = transaction['db']
                id = transaction['id']
                record = transaction['record']
                db.update(record, Query().id == id)
                return

            elif operation == 'delete':
                db = transaction['db']
                id = transaction['id']
                db.remove(Query().id == id)
                return
