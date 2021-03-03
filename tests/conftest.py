import pytest
from api import get_app
import os

from tinydb import TinyDB

test_dbs = ['testlightdb', 'testmotordb', 'testmotiondb', 'testscheduledb']

@pytest.fixture(scope="session")
def client():
    with get_app().app.test_client() as c:
        yield c

""" mock databases """

@pytest.fixture(scope="function")
def light_db(light_object):
    light_db = TinyDB('./database/testlightdb.json')

    # contains a dummy record
    light_db.insert(light_object)

    yield light_db

    os.remove('./database/testlightdb.json')

@pytest.fixture(scope="function")
def motor_db(motor_object):
    
    motor_db = TinyDB('./database/testmotordb.json')

    # contains a dummy record
    motor_db.insert(motor_object)

    yield motor_db

    os.remove('./database/testmotordb.json')

@pytest.fixture(scope="function")
def motion_db(motion_object):
    
    motion_db = TinyDB('./database/testmotiondb.json')

    # contains a dummy record
    motion_db.insert(motion_object)

    yield motion_db

    os.remove('./database/testmotiondb.json')

@pytest.fixture(scope="function")
def schedule_db(schedule_object):
    
    schedule_db = TinyDB('./database/testscheduledb.json')

    # contains a dummy record
    schedule_db.insert(schedule_object)

    yield schedule_db

    os.remove('./database/testscheduledb.json')
    
""" mock objects """

@pytest.fixture(scope='function')
def light_object():
    light_object = {}
    light_object['id'] = 0
    light_object['name'] = 'test_light'
    light_object['ip'] = '192.0.0.1'
    light_object['active'] = False
    light_object['battery'] = 89
    light_object['motor_ids'] = [0]
    light_object['style'] = 'some-icon'

    return light_object

@pytest.fixture(scope='function')
def motor_object():
    motor_object = {}
    motor_object['id'] = 0
    motor_object['name'] = 'test_motor'
    motor_object['ip'] = '192.0.0.1'
    motor_object['active'] = False
    motor_object['level'] = 100
    motor_object['battery'] = 89
    motor_object['length'] = 200
    motor_object['style'] = 'some-icon'

    return motor_object

@pytest.fixture(scope='function')
def motion_object():
    motion_object = {}
    motion_object['id'] = 0
    motion_object['duration_sensitivity'] = '00:20'
    motion_object['name'] = 'test_motion'
    motion_object['ip'] = '192.0.0.1'
    motion_object['active'] = False
    motion_object['battery'] = 89
    motion_object['motor_ids'] = [0]
    motion_object['style'] = 'some-icon'

    return motion_object

@pytest.fixture(scope='function')
def schedule_object():
    schedule_object = {}
    schedule_object['id'] = 0
    schedule_object['name'] = 'test_schedule'
    schedule_object['active'] = False
    schedule_object['days'] = ['Monday']
    schedule_object['target_level'] = 80
    schedule_object['gradient'] = 45
    schedule_object['time'] = '07:00'
    schedule_object['motor_ids'] = [0]

    return schedule_object

def pytest_sessionfinish(session, exitstatus):
    
    for test_db in test_dbs:
        try:
            os.remove(f"./database/{test_db}.json")
        except:
            pass
