from tinydb import TinyDB, Query, where
db = TinyDB('./database/light-sensors.json')
motor_db = TinyDB('./database/motors.json')


def get(light_sensor_id):
    try:
        light_sensor = db.search(Query().id == light_sensor_id)[0]

        if light_sensor:
            return light_sensor, 200
        else:
            return f"Light sensor {light_sensor_id} not found", 400
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
        all_light_sensors = db.all()
        ids = [light_sensor['id'] for light_sensor in all_light_sensors]

        if ids:
            largest_id = max(ids)
            body['id'] = largest_id + 1
        else:
            body['id'] = 0

        db.insert(body)

        new_light_sensor = db.search(Query().id == body['id'])
        return new_light_sensor, 200
    except:
        return 'Internal server error', 500


def unregister(light_sensor_id):
    try:
        light_sensor = db.search(Query().id == light_sensor_id)

        if light_sensor:
            db.remove(Query().id == light_sensor_id)
            return f"Light sensor {light_sensor_id} unregistered", 200
        else:
            return f"Light sensor {light_sensor_id} does not exist", 400
    except:
        return 'Internal server error', 500


def rename(body):
    try:
        light_sensor = db.search(Query().id == body['id'])

        if light_sensor:
            light_sensor_db_key = db.update({'name': body['name']}, Query().id == body['id'])
            return db.get(doc_id=light_sensor_db_key[0]), 200
        else:
            return f"Light sensor {body['id']} does not exist", 400
    except:
        return 'Internal server error', 500


def deactivate(light_sensor_id):
    try:
        light_sensor = db.search(Query().id == light_sensor_id)

        if light_sensor:
            light_sensor_db_key = db.update({'active': False}, Query().id == light_sensor_id)
            return db.get(doc_id=light_sensor_db_key[0]), 200
        else:
            return f"Light sensor {light_sensor_id} does not exist", 400
    except:
        return 'Internal server error', 500


def activate(light_sensor_id):
    try:
        light_sensor = db.search(Query().id == light_sensor_id)

        if light_sensor:
            light_sensor_db_key = db.update({'active': True}, Query().id == light_sensor_id)
            return db.get(doc_id=light_sensor_db_key[0]), 200
        else:
            return f"Light sensor {light_sensor_id} does not exist", 400
    except:
        return 'Internal server error', 500


def change_motors(body):
    try:
        light_sensor_id = body['id']
        motor_ids = body['motor_ids']

        print(body)

        for motor_id in motor_ids:
            motorExists = motor_db.contains(where('id') == motor_id)
            if not motorExists:
                raise Exception()

        db.update({'motor_ids': motor_ids}, Query().id == light_sensor_id)
        light_sensor = db.search(Query().id == light_sensor_id)[0]
        return light_sensor

    except:
        return 'Internal server error', 500