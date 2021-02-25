from tinydb import TinyDB, Query, where
import re
import utils

db = TinyDB('./database/motion-sensors.json')
motor_db = TinyDB('./database/motors.json')


def get(motion_sensor_id):
    try:
        motion_sensor_exists = db.contains(where('id') == motion_sensor_id)

        if motion_sensor_exists:
            motion_sensor = db.search(Query().id == motion_sensor_id)[0]
            return motion_sensor, 200
        else:
            return f"Motion sensor {motion_sensor_id} not found", 404
    except:
        return 'Internal server error', 500


def get_all():
    try:
        all_motion_sensors = db.all()
        return all_motion_sensors, 200
    except:
        return 'Internal server error', 500


def register(body):
    try:
        ip = body['ip']
        motor_ids = body['motor_ids']
        battery = body['battery']

        if not utils.valid_ip(ip):
            return f'Could not register: Invalid ip {ip}', 400

        if not (0 <= battery <= 100):
            return f'Could not register: Invalid battery level {battery}', 400

        for motor_id in motor_ids:
            motor_exists = motor_db.contains(where('id') == motor_id)
            if not motor_exists:
                return f"Could not register: Motor {motor_id} does not exist", 400

        all_motion_sensors = db.all()
        ids = [motion_sensor['id'] for motion_sensor in all_motion_sensors]

        if ids:
            largest_id = max(ids)
            body['id'] = largest_id + 1
        else:
            body['id'] = 0

        db.insert(body)

        new_motion_sensor = db.search(Query().id == body['id'])
        return new_motion_sensor, 200
    except:
        return 'Internal server error', 500


def unregister(motion_sensor_id):
    try:
        motion_sensor_exists = db.contains(where('id') == motion_sensor_id)

        if motion_sensor_exists:
            db.remove(Query().id == motion_sensor_id)
            return f"Motion sensor {motion_sensor_id} unregistered", 200
        else:
            return f"Motion sensor {motion_sensor_id} does not exist", 404
    except:
        return 'Internal server error', 500


def update(motion_sensor_id, body):
    try:
        ip = body['ip']
        motor_ids = body['motor_ids']
        battery = body['battery']

        if not utils.valid_ip(ip):
            return f'Could not register: Invalid ip {ip}', 400

        if not (0 <= battery <= 100):
            return f'Could not register: Invalid battery level {battery}', 400

        for motor_id in motor_ids:
            motor_exists = motor_db.contains(where('id') == motor_id)
            if not motor_exists:
                return f"Could not register: Motor {motor_id} does not exist", 400

        motion_sensor_exists = db.contains(where('id') == motion_sensor_id)

        if motion_sensor_exists:
            motion_sensor_db_key = db.update(body, Query().id == motion_sensor_id)
            return db.get(doc_id=motion_sensor_db_key[0]), 200
        else:
            return f"Motion sensor {motion_sensor_id} does not exist", 404
    except:
        return 'Internal server error', 500


def rename(motion_sensor_id, body):
    try:
        motion_sensor_exists = db.contains(where('id') == motion_sensor_id)

        if motion_sensor_exists:
            motion_sensor_db_key = db.update({'name': body}, Query().id == motion_sensor_id)
            return db.get(doc_id=motion_sensor_db_key[0]), 200
        else:
            return f"Motion sensor {body['id']} does not exist", 404
    except:
        return 'Internal server error', 500


def deactivate(motion_sensor_id):
    try:
        motion_sensor_exists = db.contains(where('id') == motion_sensor_id)

        if motion_sensor_exists:
            motion_sensor_db_key = db.update({'active': False}, Query().id == motion_sensor_id)
            return db.get(doc_id=motion_sensor_db_key[0]), 200
        else:
            return f"Motion sensor {motion_sensor_id} does not exist", 404
    except:
        return 'Internal server error', 500


def activate(motion_sensor_id):
    try:
        motion_sensor_exists = db.contains(where('id') == motion_sensor_id)

        if motion_sensor_exists:
            motion_sensor_db_key = db.update({'active': True}, Query().id == motion_sensor_id)
            return db.get(doc_id=motion_sensor_db_key[0]), 200
        else:
            return f"Motion sensor {motion_sensor_id} does not exist", 404
    except:
        return 'Internal server error', 500


def change_motors(motion_sensor_id, body):
    try:
        motor_ids = body

        motion_sensor_exists = db.contains(where('id') == motion_sensor_id)

        if not motion_sensor_exists:
            return f"Motion sensor {motion_sensor_id} does not exist", 404

        for motor_id in motor_ids:
            motor_exists = motor_db.contains(where('id') == motor_id)
            if not motor_exists:
                return f"Motor {motor_id} does not exist", 404

        db.update({'motor_ids': motor_ids}, Query().id == motion_sensor_id)
        motion_sensor = db.search(Query().id == motion_sensor_id)[0]
        return motion_sensor, 200

    except:
        return 'Internal server error', 500
    

def change_duration_sensitivity(motion_sensor_id, body):
    duration_sensitivity = body

    if not db.contains(where('id') == motion_sensor_id):
        return f"Motion sensor {motion_sensor_id} does not exist", 400

    pattern = re.compile("[0-9][0-9][:][0-9][0-9]")
    correct_format = pattern.match(duration_sensitivity)

    if not correct_format:
        return f"{duration_sensitivity} is not a valid hh:mm format", 400

    db.update({'duration_sensitivity': duration_sensitivity}, Query().id == motion_sensor_id)
    motion_sensor = db.search(Query().id == motion_sensor_id)[0]
    return motion_sensor
