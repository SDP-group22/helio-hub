from tinydb import TinyDB, Query, where

db = TinyDB('./database/schedule.json')


def get_all():
    try:
        all_schedules = db.all()
        return all_schedules, 200
    except:
        return 'Internal server error', 500


def register(body):
    try:
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
        schedule = db.search(Query().id == schedule_id)

        if schedule:
            db.remove(Query().id == schedule_id)
            return f"Schedule {schedule_id} unregistered", 200
        else:
            return f"Schedule {schedule_id} does not exist", 400
    except:
        return 'Internal server error', 500


def change_days(schedule_id, body):
    try:
        days = body

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

        db.update({'gradient': gradient}, Query().id == schedule_id)
        schedule = db.search(Query().id == schedule_id)[0]
        return schedule

    except:
        return 'Internal server error', 500


def rename(schedule_id, body):
    try:
        name = body
        schedule = db.search(Query().id == schedule_id)

        if schedule:
            schedule_db_key = db.update({'name': name}, Query().id == schedule_id)
            return db.get(doc_id=schedule_db_key[0]), 200
        else:
            return f"Schedule {schedule_id} does not exist", 400
    except:
        return 'Internal server error', 500


def activate(schedule_id):
    try:
        schedule = db.search(Query().id == schedule_id)

        if schedule:
            schedule_db_key = db.update({'active': True}, Query().id == schedule_id)
            return db.get(doc_id=schedule_db_key[0]), 200
        else:
            return f"Schedule {schedule_id} does not exist", 400
    except:
        return 'Internal server error', 500


def deactivate(schedule_id):
    try:
        schedule = db.search(Query().id == schedule_id)

        if schedule:
            schedule_db_key = db.update({'active': False}, Query().id == schedule_id)
            return db.get(doc_id=schedule_db_key[0]), 200
        else:
            return f"Schedule {schedule_id} does not exist", 400
    except:
        return 'Internal server error', 500
