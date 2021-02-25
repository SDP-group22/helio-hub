from tinydb import TinyDB, Query
db = TinyDB('./database/motors.json')

def get(motor_id):
    try:
        # db search returns a list
        motor = db.search(Query().id == motor_id)
        
        if motor:
            return motor[0], 200
        else:
            return f"Motor {motor_id} not found", 400
    except:
        return 'Internal server error', 500

def get_all():
    try:
        all_motors = db.all()
        return all_motors, 200
    except:
        return 'Internal server error', 500

def register(body):
    try:

        # TODO confirm motor is available at given ip, if not return 400

        # generate new id by incrementing on largest existing id
        all_motors = db.all()
        ids = [motor['id'] for motor in all_motors]
        
        if ids:
            largest_id = max(ids)
            body['id'] = largest_id + 1
        else:
            # if database empty start id at 0
            body['id'] = 0

        # Add new motor to database
        db.insert(body)

        new_motor = db.search(Query().id == body['id'])[0]
        return new_motor, 200
    except:
        return 'Internal server error', 500

def unregister(motor_id):
    try:
        motor = db.search(Query().id == motor_id)

        if motor:

            # TODO call unregister on motor api, if fail return 400

            db.remove(Query().id == motor_id)
            return f"Motor {motor_id} unregistered", 200
        else:
            return f"Motor {motor_id} does not exist", 400
    except:
        return 'Internal server error', 500

def update(motor_id, body):
    try:
        motor = db.search(Query().id == motor_id)

        if motor:
            motor_db_key = db.update(body, Query().id==motor_id)
            return db.get(doc_id=motor_db_key[0]), 200
        else:
            return f"Motor {motor_id} does not exist", 400
    except:
        return 'Internal server error', 500  

def move(motor_id, body):
    try:
        motor = db.search(Query().id == motor_id)
        level = body

        if motor:

            # TODO call move on motor api, if fail return 400

            motor_db_key = db.update({'level':level}, Query().id==motor_id)
            return db.get(doc_id=motor_db_key[0]), 200
        else:
            return f"Motor {motor_id} does not exist", 400
    except:
        return 'Internal server error', 500

def rename(motor_id, body):
    try:
        motor = db.search(Query().id == motor_id)
        name = body

        if motor:
            motor_db_key = db.update({'name':name}, Query().id==motor_id)
            return db.get(doc_id=motor_db_key[0]), 200
        else:
            return f"Motor {motor_id} does not exist", 400
    except:
        return 'Internal server error', 500

def deactivate(motor_id):
    try:
        motor = db.search(Query().id == motor_id)

        if motor:

            # TODO call deactivate on motor api, if fail return 400

            motor_db_key = db.update({'active':False}, Query().id==motor_id)
            return db.get(doc_id=motor_db_key[0]), 200
        else:
            return f"Motor {motor_id} does not exist", 400
    except:
        return 'Internal server error', 500

def activate(motor_id):
    try:
        motor = db.search(Query().id == motor_id)

        if motor:
            # TODO call activate on motor api, if fail return 400
            motor_db_key = db.update({'active':True}, Query().id==motor_id)
            return db.get(doc_id=motor_db_key[0]), 200
        else:
            return f"Motor {motor_id} does not exist", 400
    except:
        return 'Internal server error', 500

def start_calibration(motor_id):
    pass

def stop_calibration(motor_id):
    pass