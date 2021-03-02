from tinydb import TinyDB, Query, where
import utils

db = TinyDB('./database/light-sensors.json')
motor_db = TinyDB('./database/motors.json')


def get(light_sensor_id):
    try:
        light_sensor = db.search(Query().id == light_sensor_id)

        if light_sensor:
            return light_sensor[0], 200
        else:
            return f"Light sensor {light_sensor_id} not found", 404
    except:
        return 'Internal server error', 500


def get_all():
    try:
        all_light_sensors = db.all()
        return all_light_sensors, 200
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

        all_light_sensors = db.all()
        ids = [light_sensor['id'] for light_sensor in all_light_sensors]

        if ids:
            largest_id = max(ids)
            body['id'] = largest_id + 1
        else:
            body['id'] = 0

        db.insert(body)

        new_light_sensor = db.search(Query().id == body['id'])[0]
        return new_light_sensor, 200
    except:
        return 'Internal server error', 500


def unregister(light_sensor_id):
    try:
        light_sensor_exists = db.contains(where('id') == light_sensor_id)

        if light_sensor_exists:
            db.remove(Query().id == light_sensor_id)
            return f"Light sensor {light_sensor_id} unregistered", 200
        else:
            return f"Light sensor {light_sensor_id} does not exist", 404
    except:
        return 'Internal server error', 500


def update(light_sensor_id, body):
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

        light_sensor_exists = db.contains(where('id') == light_sensor_id)

        if light_sensor_exists:
            light_sensor_db_key = db.update(body, Query().id == light_sensor_id)
            return db.get(doc_id=light_sensor_db_key[0]), 200
        else:
            return f"Light sensor {light_sensor_id} does not exist", 404
    except:
        return 'Internal server error', 500


def rename(light_sensor_id, body):
    try:
        light_sensor_exists = db.contains(where('id') == light_sensor_id)

        if light_sensor_exists:
            light_sensor_db_key = db.update({'name': body}, Query().id == light_sensor_id)
            return db.get(doc_id=light_sensor_db_key[0]), 200
        else:
            return f"Light sensor {light_sensor_id} does not exist", 404
    except:
        return 'Internal server error', 500


def deactivate(light_sensor_id):
    try:
        light_sensor_exists = db.contains(where('id') == light_sensor_id)

        if light_sensor_exists:
            light_sensor_db_key = db.update({'active': False}, Query().id == light_sensor_id)
            return db.get(doc_id=light_sensor_db_key[0]), 200
        else:
            return f"Light sensor {light_sensor_id} does not exist", 404
    except:
        return 'Internal server error', 500


def activate(light_sensor_id):
    try:
        light_sensor_exists = db.contains(where('id') == light_sensor_id)

        if light_sensor_exists:
            light_sensor_db_key = db.update({'active': True}, Query().id == light_sensor_id)
            return db.get(doc_id=light_sensor_db_key[0]), 200
        else:
            return f"Light sensor {light_sensor_id} does not exist", 404
    except:
        return 'Internal server error', 500


def change_motors(light_sensor_id, body):
    try:
        motor_ids = body

        light_sensor_exists = db.contains(where('id') == light_sensor_id)

        if not light_sensor_exists:
            return f"Light sensor {light_sensor_id} does not exist", 404

        for motor_id in motor_ids:
            motor_exists = motor_db.contains(where('id') == motor_id)
            if not motor_exists:
                return f"Motor {motor_id} does not exist", 404

        db.update({'motor_ids': motor_ids}, Query().id == light_sensor_id)
        light_sensor = db.search(Query().id == light_sensor_id)[0]
        return light_sensor, 200

    except:
        return 'Internal server error', 500
