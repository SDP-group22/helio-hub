from tinydb import TinyDB, Query
db = TinyDB('./database/motors.json')

def get(motor_id):
    motor = db.search(Query().id == motor_id)
    return motor

def register(body):
    db.insert(body)
    return body

def unregister(motor_id):
    db.remove(Query().id == motor_id)
    return 200

def move(body):
    motor_db_key = db.update({'level':body['level']}, Query().id==body['id'])
    return db.get(doc_id=motor_db_key[0])

def rename(body):
    motor_db_key = db.update({'name':body['name']}, Query().id==body['id'])
    return db.get(doc_id=motor_db_key[0])

def deactivate(body):
    motor_db_key = db.update({'active':False}, Query().id==body['id'])
    return db.get(doc_id=motor_db_key[0])

def activate(body):
    motor_db_key = db.update({'active':True}, Query().id==body['id'])
    return db.get(doc_id=motor_db_key[0])

def start_calibration(body):
    pass

def stop_calibration(body):
    pass