from tinydb import TinyDB, Query, where
from db_handler import DbHandler
import utils

db = TinyDB('./database/schedule.json')
motor_db = TinyDB('./database/motors.json')

def get_all():
    try:
        db_handler = DbHandler.get_instance()
        all_schedules = db_handler.read_all(db)
        return all_schedules, 200
    except:
        return 'Internal server error', 500


def register(body):
    try:
        motor_ids = body['motor_ids']
        days = body['days']
        gradient = body['gradient']
        target_level = body['target_level']

        for day in days:
            if not utils.valid_day(day):
                return f"Could not register: Invalid day {day}", 400

        if not 0 <= gradient:
            return f"Could not register: Invalid gradient {gradient}", 400

        if not 0 <= target_level <= 100:
            return f"Could not register: Invalid target level {target_level}", 400

        db_handler = DbHandler.get_instance()

        for motor_id in motor_ids:
            motor_exists = db_handler.contains(motor_db, motor_id)
            if not motor_exists:
                return f"Could not register: Motor {motor_id} does not exist", 400

        all_schedules = db_handler.read_all(db)
        ids = [schedule['id'] for schedule in all_schedules]

        if ids:
            largest_id = max(ids)
            body['id'] = largest_id + 1
        else:
            body['id'] = 0

        db_handler.write(db, body)

        new_schedule = db_handler.read(db, body['id'])
        return new_schedule, 200
    except:
        return 'Internal server error', 500


def unregister(schedule_id):
    try:
        db_handler = DbHandler.get_instance()
        schedule_exists = db_handler.contains(db, schedule_id)

        if schedule_exists:
            db_handler.delete(db, schedule_id)

            return f"Schedule {schedule_id} unregistered", 200
        else:
            return f"Schedule {schedule_id} does not exist", 404
    except:
        return 'Internal server error', 500


def update(schedule_id, body):
    try:

        motor_ids = body['motor_ids']
        days = body['days']
        gradient = body['gradient']
        target_level = body['target_level']

        for day in days:
            if not utils.valid_day(day):
                return f"Could not register: Invalid day {day}", 400

        if not 0 <= gradient:
            return f"Could not register: Invalid gradient {gradient}", 400

        if not 0 <= target_level <= 100:
            return f"Could not register: Invalid target level {target_level}", 400

        db_handler = DbHandler.get_instance()

        for motor_id in motor_ids:
            motor_exists = db_handler.contains(motor_db, motor_id)
            if not motor_exists:
                return f"Could not register: Motor {motor_id} does not exist", 400

        schedule_exists = db_handler.contains(db, schedule_id)

        if schedule_exists:
            db_handler.update(db, schedule_id, body)

            updated_schedule = db_handler.read(db, schedule_id)

            return updated_schedule, 200
        else:
            return f"Schedule {schedule_id} does not exist", 404
    except:
        return 'Internal server error', 500
