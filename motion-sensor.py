from tinydb import TinyDB, Query, where
from db_handler import DbHandler
import re
import utils

db = TinyDB('./database/motion-sensors.json')
motor_db = TinyDB('./database/motors.json')


def get(motion_sensor_id):
    try:
        db_handler = DbHandler.get_instance()
        motion_sensor_exists = db_handler.contains(db, motion_sensor_id)

        if motion_sensor_exists:
            motion_sensor = db_handler.read(db, motion_sensor_id)
            return motion_sensor, 200
        else:
            return f"Motion sensor {motion_sensor_id} not found", 404
    except:
        return 'Internal server error', 500


def get_all():
    try:
        db_handler = DbHandler.get_instance()
        all_motion_sensors = db_handler.read_all(db)
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

        db_handler = DbHandler.get_instance()

        for motor_id in motor_ids:
            motor_exists = db_handler.contains(motor_db, motor_id)
            if not motor_exists:
                return f"Could not register: Motor {motor_id} does not exist", 400

        all_motion_sensors = db_handler.read_all(db)
        ids = [motion_sensor['id'] for motion_sensor in all_motion_sensors]

        if ids:
            largest_id = max(ids)
            body['id'] = largest_id + 1
        else:
            body['id'] = 0

        db_handler.write(db, body)

        new_motion_sensor = db_handler.read(db, body['id'])
        return new_motion_sensor, 200
    except:
        return 'Internal server error', 500


def unregister(motion_sensor_id):
    try:
        db_handler = DbHandler.get_instance()
        motion_sensor_exists = db_handler.contains(db, motion_sensor_id)

        if motion_sensor_exists:
            db_handler.delete(db, motion_sensor_id)

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

        db_handler = DbHandler.get_instance()

        for motor_id in motor_ids:
            motor_exists = db_handler.contains(motor_db, motor_id)
            if not motor_exists:
                return f"Could not register: Motor {motor_id} does not exist", 400

        motion_sensor_exists = db_handler.contains(db, motion_sensor_id)

        if motion_sensor_exists:
            db_handler.update(db, motion_sensor_id, body)

            updated_motion_sensor = db_handler.read(db, motion_sensor_id)

            return updated_motion_sensor, 200
        else:
            return f"Motion sensor {motion_sensor_id} does not exist", 404
    except:
        return 'Internal server error', 500
