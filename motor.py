from tiny_db_wrapper import *

def get(motor_id):
    try:
        # db.search returns a list
        motor = motor_table.search(Query().id == motor_id)
        
        if motor:
            return motor[0], 200
        else:
            return f"Motor {motor_id} not found", 400
    except:
        return 'Internal server error', 500

def get_all():
    try:
        all_motors = motor_table.all()
        return all_motors, 200
    except:
        return 'Internal server error', 500

def register(body):
    try:

        # TODO confirm motor is available at given ip, if not return 400

        # generate new id by incrementing on largest existing id
        all_motors = motor_table.all()
        ids = [motor['id'] for motor in all_motors]
        
        if ids:
            largest_id = max(ids)
            body['id'] = largest_id + 1
        else:
            # if database empty start id at 0
            body['id'] = 0

        # Add new motor to database
        motor_table.insert(body)

        new_motor = motor_table.search(Query().id == body['id'])
        return new_motor, 200
    except:
        return 'Internal server error', 500

def unregister(motor_id):
    try:
        motor = motor_table.search(Query().id == motor_id)

        if motor:

            # TODO call unregister on motor api, if fail return 400

            motor_table.remove(Query().id == motor_id)
            return f"Motor {motor_id} unregistered", 200
        else:
            return f"Motor {motor_id} does not exist", 400
    except:
        return 'Internal server error', 500
    
def move(body):
    try:
        motor = motor_table.search(Query().id == body['id'])

        if motor:

            # TODO call move on motor api, if fail return 400

            motor_db_key = motor_table.update({'level':body['level']}, Query().id==body['id'])
            return motor_table.get(doc_id=motor_db_key[0]), 200
        else:
            return f"Motor {body['id']} does not exist", 400
    except:
        return 'Internal server error', 500

def rename(body):
    try:
        motor = motor_table.search(Query().id == body['id'])

        if motor:
            motor_db_key = motor_table.update({'name':body['name']}, Query().id==body['id'])
            return motor_table.get(doc_id=motor_db_key[0]), 200
        else:
            return f"Motor {body['id']} does not exist", 400
    except:
        return 'Internal server error', 500

def deactivate(motor_id):
    try:
        motor = motor_table.search(Query().id == motor_id)

        if motor:

            # TODO call deactivate on motor api, if fail return 400

            motor_db_key = motor_table.update({'active':False}, Query().id==motor_id)
            return motor_table.get(doc_id=motor_db_key[0]), 200
        else:
            return f"Motor {motor_id} does not exist", 400
    except:
        return 'Internal server error', 500

def activate(motor_id):
    try:
        motor = motor_table.search(Query().id == motor_id)

        if motor:
            # TODO call activate on motor api, if fail return 400
            motor_db_key = motor_table.update({'active':True}, Query().id==motor_id)
            return motor_table.get(doc_id=motor_db_key[0]), 200
        else:
            return f"Motor {motor_id} does not exist", 400
    except:
        return 'Internal server error', 500

def start_calibration(motor_id):
    pass

def stop_calibration(motor_id):
    pass