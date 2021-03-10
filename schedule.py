from tinydb import TinyDB, Query, where
from db_writer import DbWriter
import utils

db = TinyDB('./database/schedule.json')
motor_db = TinyDB('./database/motors.json')

def get_all():
    try:
        all_schedules = db.all()
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

        for motor_id in motor_ids:
            motor_exists = motor_db.contains(where('id') == motor_id)
            if not motor_exists:
                return f"Could not register: Motor {motor_id} does not exist", 400

        all_schedules = db.all()
        ids = [schedule['id'] for schedule in all_schedules]

        if ids:
            largest_id = max(ids)
            body['id'] = largest_id + 1
        else:
            body['id'] = 0

        dbWriter = DbWriter.get_instance()
        dbWriter.write_to_db(db, body)
        dbWriter.queue.join()

        new_schedule = db.search(Query().id == body['id'])[0]
        return new_schedule, 200
    except:
        return 'Internal server error', 500


def unregister(schedule_id):
    try:
        schedule_exists = db.contains(where('id') == schedule_id)

        if schedule_exists:
            dbWriter = DbWriter.get_instance()
            dbWriter.delete_from_db(db, schedule_id)
            dbWriter.queue.join()
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

        for motor_id in motor_ids:
            motor_exists = motor_db.contains(where('id') == motor_id)
            if not motor_exists:
                return f"Could not register: Motor {motor_id} does not exist", 400

        schedule_exists = db.contains(where('id') == schedule_id)

        if schedule_exists:
            dbWriter = DbWriter.get_instance()
            dbWriter.update_db(db, schedule_id, body)
            dbWriter.queue.join()

            return db.get(Query().id == schedule_id), 200
        else:
            return f"Schedule {schedule_id} does not exist", 404
    except:
        return 'Internal server error', 500
