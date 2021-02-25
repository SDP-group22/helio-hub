from tinydb import TinyDB, Query, where
import utils

db = TinyDB('./database/schedule.json')

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

        db.insert(body)

        new_schedule = db.search(Query().id == body['id'])[0]
        return new_schedule, 200
    except:
        return 'Internal server error', 500


def unregister(schedule_id):
    try:
        schedule_exists = db.contains(where('id') == schedule_id)

        if schedule_exists:
            db.remove(Query().id == schedule_id)
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
            schedule_db_key = db.update(body, Query().id == schedule_id)
            return db.get(doc_id=schedule_db_key[0]), 200
        else:
            return f"Schedule {schedule_id} does not exist", 404
    except:
        return 'Internal server error', 500


def rename(schedule_id, body):
    try:
        schedule_exists = db.contains(where('id') == schedule_id)

        if schedule_exists:
            schedule_db_key = db.update({'name': body}, Query().id == schedule_id)
            return db.get(doc_id=schedule_db_key[0]), 200
        else:
            return f"Schedule {body['id']} does not exist", 404
    except:
        return 'Internal server error', 500


def deactivate(schedule_id):
    try:
        schedule_exists = db.contains(where('id') == schedule_id)

        if schedule_exists:
            schedule_db_key = db.update({'active': False}, Query().id == schedule_id)
            return db.get(doc_id=schedule_db_key[0]), 200
        else:
            return f"Schedule {schedule_id} does not exist", 404
    except:
        return 'Internal server error', 500


def activate(schedule_id):
    try:
        schedule_exists = db.contains(where('id') == schedule_id)

        if schedule_exists:
            schedule_db_key = db.update({'active': True}, Query().id == schedule_id)
            return db.get(doc_id=schedule_db_key[0]), 200
        else:
            return f"Schedule {schedule_id} does not exist", 404
    except:
        return 'Internal server error', 500


def change_days(schedule_id, body):
    try:
        days = body

        for day in days:
            if not utils.valid_day(day):
                return f"Could not change days: Invalid day {day}", 400

        db.update({'days': days}, Query().id == schedule_id)
        schedule = db.search(Query().id == schedule_id)[0]
        return schedule

    except:
        return 'Internal server error', 500


def change_time(schedule_id, body):
    try:
        time = body

        db.update({'time': time}, Query().id == schedule_id)
        schedule = db.search(Query().id == schedule_id)[0]
        return schedule

    except:
        return 'Internal server error', 500


def change_gradient(schedule_id, body):
    try:
        gradient = body

        if not 0 <= gradient:
            return f"Could not change gradient: Invalid gradient {gradient}", 400

        db.update({'gradient': gradient}, Query().id == schedule_id)
        schedule = db.search(Query().id == schedule_id)[0]
        return schedule

    except:
        return 'Internal server error', 500
