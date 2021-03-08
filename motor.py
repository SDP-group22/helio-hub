from tinydb import TinyDB, Query, where
import utils

db = TinyDB('./database/motors.json')


def get(motor_id):
    try:
        # db search returns a list
        motor = db.search(Query().id == motor_id)
        
        if motor:
            return motor[0], 200
        else:
            return f"Motor {motor_id} not found", 404
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
        ip = body['ip']
        battery = body['battery']
        level = body['level']

        if not utils.valid_ip(ip):
            return f'Could not register: Invalid ip {ip}', 400

        if not (0 <= battery <= 100):
            return f'Could not register: Invalid battery level {battery}', 400

        if not (0 <= level <= 100):
            return f'Could not register: Invalid level {level}', 400

        all_motors = db.all()
        ids = [motor['id'] for motor in all_motors]

        if ids:
            largest_id = max(ids)
            body['id'] = largest_id + 1
        else:
            body['id'] = 0

        db.insert(body)

        new_motor = db.search(Query().id == body['id'])[0]
        return new_motor, 200
    except Exception as e:
        print(str(e))
        return 'Internal server error', 500


def unregister(motor_id):
    try:
        motor_exists = db.contains(where('id') == motor_id)

        if motor_exists:
            db.remove(Query().id == motor_id)
            return f"Motor {motor_id} unregistered", 200
        else:
            return f"Motor {motor_id} does not exist", 404
    except:
        return 'Internal server error', 500


def update(motor_id, body):
    try:
        ip = body['ip']
        battery = body['battery']
        level = body['level']

        if not utils.valid_ip(ip):
            return f'Could not register: Invalid ip {ip}', 400

        if not (0 <= battery <= 100):
            return f'Could not register: Invalid battery level {battery}', 400

        if not (0 <= level <= 100):
            return f'Could not register: Invalid level {level}', 400

        motor_exists = db.contains(where('id') == motor_id)

        if motor_exists:
            motor_db_key = db.update(body, Query().id == motor_id)
            return db.get(doc_id=motor_db_key[0]), 200
        else:
            return f"Motor {motor_id} does not exist", 404
    except:
        return 'Internal server error', 500


def rename(motor_id, body):
    try:
        motor_exists = db.contains(where('id') == motor_id)

        if motor_exists:
            motor_db_key = db.update({'name': body}, Query().id == motor_id)
            return db.get(doc_id=motor_db_key[0]), 200
        else:
            return f"Motor {body['id']} does not exist", 404
    except Exception as e:
        print(str(e))
        return 'Internal server error', 500


def deactivate(motor_id):
    try:
        motor_exists = db.contains(where('id') == motor_id)

        if motor_exists:
            motor_db_key = db.update({'active': False}, Query().id == motor_id)
            return db.get(doc_id=motor_db_key[0]), 200
        else:
            return f"Motor {motor_id} does not exist", 404
    except:
        return 'Internal server error', 500


def activate(motor_id):
    try:
        motor_exists = db.contains(where('id') == motor_id)

        if motor_exists:
            motor_db_key = db.update({'active': True}, Query().id == motor_id)
            return db.get(doc_id=motor_db_key[0]), 200
        else:
            return f"Motor {motor_id} does not exist", 404
    except:
        return 'Internal server error', 500


def move(motor_id, body):
    try:
        motor_exists = db.contains(where('id') == motor_id)

        if motor_exists:
            level = body

            motor_db_key = db.update({'level': level}, Query().id == motor_id)
            return db.get(doc_id=motor_db_key[0]), 200
        else:
            return f"Motor {body['id']} does not exist", 404

    except:
        return 'Internal server error', 500


def calibration_start(motor_id):
    print('start calibration')
    return 'start calibration', 200

def calibration_stop(motor_id):
    print('stop calibration')
    return 'stop calibration', 200

def calibration_move_up(motor_id):
    print('moving up calibration')
    return 'moving up calibration', 200

def calibration_move_down(motor_id):
    print('moving down calibration')
    return 'moving down calibration', 200

def calibration_stop_moving(motor_id):
    print('stop calibration moving')
    return 'stop calibration moving', 200

def calibration_set_highest(motor_id):
    print('highest set')
    return 'highest set', 200

def calibration_set_lowest(motor_id):
    print('lowest set')
    return 'lowest set', 200