import queue
import threading
from tinydb import Query


class DbWriter(threading.Thread):
    instance = None

    @staticmethod
    def make_instance():
        if DbWriter.instance is None:
            q = queue.Queue()
            DbWriter.instance = DbWriter(q)
            DbWriter.instance.daemon = True
            DbWriter.instance.name = 'DbWriterThread'

    @staticmethod
    def get_instance():
        return DbWriter.instance

    @staticmethod
    def has_instance():
        return DbWriter.instance is not None

    @staticmethod
    def is_running():
        return DbWriter.instance.is_alive()

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def write_to_db(self, db, record):
        self.queue.put({'db': db, 'record': record, 'operation': 'write'})

    def update_db(self, db, id, record):
        self.queue.put({'db': db, 'id': id, 'record': record, 'operation': 'update'})

    def delete_from_db(self, db, id):
        self.queue.put({'db': db, 'id': id, 'operation': 'delete'})

    def run(self):
        while True:
            try:
                task = self.queue.get()
                operation = task['operation']

                if operation == 'write':
                    db = task['db']
                    record = task['record']

                    db.insert(record)
                elif operation == 'update':
                    db = task['db']
                    id = task['id']
                    record = task['record']

                    db.update(record, Query().id == id)
                elif operation == 'delete':
                    db = task['db']
                    id = task['id']

                    db.remove(Query().id == id)

                self.queue.task_done()
            except queue.Queue.Empty:
                pass
