from tiny_db_wrapper import *
from datetime import datetime

def get(schedule_id):
    try:
        # search() returns a list
        schedule = schedule_table.search(Query().id == schedule_id)
        
        if schedule:
            return schedule[0], 200
        else:
            return f"Schedule {schedule_id} not found", 400
    except:
        return 'Internal server error', 500

def get_all():
    try:
        all_schedules = schedule_table.all()
        return all_schedules, 200
    except:
        return 'Internal server error', 500

def register(body):
    try:

        # check all corresponding motors exist
        for motor_id in body['motor-ids']:
            motor = motor_table.search(Query().id == motor_id)
            if not motor:
                return f"Motor {motor_id} not found", 400

        # generate new id by incrementing on largest existing id
        all_schedules = schedule_table.all()
        ids = [schedule['id'] for schedule in all_schedules]
        
        if ids:
            largest_id = max(ids)
            body['id'] = largest_id + 1
        else:
            # if database empty start id at 0
            body['id'] = 0

        # add last modified field
        body['last_modified'] = str(datetime.now())

        # Add new schedule to database
        schedule_table.insert(body)

        new_schedule = schedule_table.search(Query().id == body['id'])
        return new_schedule, 200
    except:
        return 'Internal server error', 500

def unregister(schedule_id):
    try:
        schedule = schedule_table.search(Query().id == schedule_id)

        if schedule:
            schedule_table.remove(Query().id == schedule_id)
            return f"Schedule {schedule_id} unregistered", 200
        else:
            return f"Schedule {schedule_id} does not exist", 400
    except:
        return 'Internal server error', 500

def change_days(body):
    try:
        schedule = schedule_table.search(Query().id == body['id'])

        if schedule:
            schedule_db_key = schedule_table.update({'days':body['days'],'last_modified':str(datetime.now())}, Query().id==body['id'])
            return schedule_table.get(doc_id=schedule_db_key[0]), 200
        else:
            return f"Schedule {body['id']} does not exist", 400
    except:
        return 'Internal server error', 500

def change_time(body):
    try:
        schedule = schedule_table.search(Query().id == body['id'])

        if schedule:
            schedule_db_key = schedule_table.update({'time':body['time'],'last_modified':str(datetime.now())}, Query().id==body['id'])
            return schedule_table.get(doc_id=schedule_db_key[0]), 200
        else:
            return f"Schedule {body['id']} does not exist", 400
    except:
        return 'Internal server error', 500

def change_gradient(body):
    try:
        schedule = schedule_table.search(Query().id == body['id'])

        if schedule:
            schedule_db_key = schedule_table.update({'gradient':body['gradient'],'last_modified':str(datetime.now())}, Query().id==body['id'])
            return schedule_table.get(doc_id=schedule_db_key[0]), 200
        else:
            return f"Schedule {body['id']} does not exist", 400
    except:
        return 'Internal server error', 500

def rename(body):
    try:
        schedule = schedule_table.search(Query().id == body['id'])

        if schedule:
            schedule_db_key = schedule_table.update({'name':body['name'],'last_modified':str(datetime.now())}, Query().id==body['id'])
            return schedule_table.get(doc_id=schedule_db_key[0]), 200
        else:
            return f"schedule {body['id']} does not exist", 400
    except:
        return 'Internal server error', 500

def activate(schedule_id):
    try:
        schedule = schedule_table.search(Query().id == schedule_id)

        if schedule:
            schedule_db_key = schedule_table.update({'active':True,'last_modified':str(datetime.now())}, Query().id==schedule_id)
            return schedule_table.get(doc_id=schedule_db_key[0]), 200
        else:
            return f"schedule {schedule_id} does not exist", 400
    except:
        return 'Internal server error', 500

def deactivate(schedule_id):
    try:
        schedule = schedule_table.search(Query().id == schedule_id)

        if schedule:
            schedule_db_key = schedule_table.update({'active':False,'last_modified':str(datetime.now())}, Query().id==schedule_id)
            return schedule_table.get(doc_id=schedule_db_key[0]), 200
        else:
            return f"schedule {schedule_id} does not exist", 400
    except:
        return 'Internal server error', 500