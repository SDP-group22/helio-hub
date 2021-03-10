from tinydb import TinyDB, Query, where
from db_writer import DbWriter
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

        dbWriter = DbWriter.get_instance()
        dbWriter.write_to_db(db, body)
        dbWriter.queue.join()

        new_motion_sensor = db.search(Query().id == body['id'])[0]
        return new_motion_sensor, 200
    except:
        return 'Internal server error', 500


def unregister(motion_sensor_id):
    try:
        motion_sensor_exists = db.contains(where('id') == motion_sensor_id)

        if motion_sensor_exists:
            dbWriter = DbWriter.get_instance()
            dbWriter.delete_from_db(db, motion_sensor_id)
            dbWriter.queue.join()
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
            dbWriter = DbWriter.get_instance()
            dbWriter.update_db(db, motion_sensor_id, body)
            dbWriter.queue.join()

            return db.get(Query().id == motion_sensor_id), 200
        else:
            return f"Motion sensor {motion_sensor_id} does not exist", 404
    except:
        return 'Internal server error', 500
