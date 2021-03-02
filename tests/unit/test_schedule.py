from api import get_app
import pytest
import json
from mock import patch
from tinydb import TinyDB
import os

@pytest.fixture(scope='module', autouse=True)
def setup():
    # delete test databases
    os.remove('./database/testmotiondb.json')
    os.remove('./database/testlightdb.json')
    os.remove('./database/testscheduledb.json')
    os.remove('./database/testmotordb.json')

    # create test database
    TinyDB('./database/testscheduledb.json')
    
    mock_motor_db = TinyDB('./database/testmotordb.json')
    mock_motor = {'id':0}
    mock_motor_db.insert(mock_motor)

@pytest.fixture(scope="module")
def client():
    with get_app().app.test_client() as c:
        yield c
    
    # teardown
    os.remove('./database/testscheduledb.json')

@pytest.fixture(scope='module')
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

"""NOTE: the order of tests is important!!!"""

@patch('schedule.db', TinyDB('./database/testscheduledb.json'))
def test_get_returns_400(schedule_object, client):
    response = client.get('/schedule/0')
    
    assert response.status_code == 400

@patch('schedule.db', TinyDB('./database/testscheduledb.json'))
def test_get_all_returns_empty_list(schedule_object, client):
    response = client.get('/schedule/get_all')
    
    assert response.json == []

@patch('schedule.db', TinyDB('./database/testscheduledb.json'))
def test_get_all_returns_200_when_db_empty(schedule_object, client):
    response = client.get('/schedule/get_all')
    
    assert response.status_code == 200

@patch('schedule.db', TinyDB('./database/testscheduledb.json'))
@patch('schedule.motor_db', TinyDB('./database/testmotordb.json'))
def test_register_returns_200(schedule_object, client):
    response = client.post('/schedule/register',
                        data=json.dumps(schedule_object),
                        content_type='application/json')

    assert response.status_code == 200

@patch('schedule.db', TinyDB('./database/testscheduledb.json'))
def test_get_returns_200(schedule_object, client):
    response = client.get('/schedule/0')
    
    assert response.status_code == 200

@patch('schedule.db', TinyDB('./database/testscheduledb.json'))
def test_get_returns_schedule_object(schedule_object, client):
    response = client.get('/schedule/0')
    
    assert response.json == schedule_object

@patch('schedule.db', TinyDB('./database/testscheduledb.json'))
def test_get_all_returns_schedule_in_list(schedule_object, client):
    response = client.get('/schedule/get_all')
    
    assert response.json == [schedule_object]

@patch('schedule.motor_db', TinyDB('./database/testmotordb.json'))
@patch('schedule.db', TinyDB('./database/testscheduledb.json'))
def test_register_increments_schedule_id(schedule_object, client):
    response = client.post('/schedule/register',
                        data=json.dumps(schedule_object),
                        content_type='application/json')
    
    assert response.json['id'] == 1

@patch('schedule.db', TinyDB('./database/testscheduledb.json'))
def test_unregister_returns_200_when_schedule_found(schedule_object, client):
    response = client.delete('/schedule/unregister/1')
    
    assert response.status_code == 200

@patch('schedule.db', TinyDB('./database/testscheduledb.json'))
def test_unregister_returns_404_when_schedule_not_found(schedule_object, client):
    response = client.delete('/schedule/unregister/1')
    
    assert response.status_code == 404

@patch('schedule.motor_db', TinyDB('./database/testmotordb.json'))
@patch('schedule.db', TinyDB('./database/testscheduledb.json'))
def test_update_returns_200_when_schedule_found(schedule_object, client):
    
    response = client.patch('/schedule/update/0',
                        data=json.dumps(schedule_object),
                        content_type='application/json')
    
    assert response.status_code == 200

# @patch('schedule.db', TinyDB('./database/testscheduledb.json'))
# def test_update_updates_name(schedule_object, client):
    
#     update_content = {'name': 'updated'}

#     response = client.patch('/schedule/update/0',
#                         data=json.dumps(update_content),
#                         content_type='application/json')
    
#     assert response.json['name'] == 'updated'

# @patch('schedule.db', TinyDB('./database/testscheduledb.json'))
# def test_update_returns_404_when_schedule_not_found(schedule_object, client):
    
#     update_content = {'name': 'updated'}

#     response = client.patch('/schedule/update/99',
#                         data=json.dumps(update_content),
#                         content_type='application/json')
    
#     assert response.status_code == 404

@patch('schedule.db', TinyDB('./database/testscheduledb.json'))
def test_deactivate_returns_200_when_schedule_found(schedule_object, client):
    response = client.patch('/schedule/deactivate/0')

    assert response.status_code == 200

@patch('schedule.db', TinyDB('./database/testscheduledb.json'))
def test_deactivate_returns_404_when_schedule_not_found(schedule_object, client):
    response = client.patch('/schedule/deactivate/99')

    assert response.status_code == 404

# @pytest.mark.skip(reason='Teardown function')
# def test_teardown():
#     os.remove('./database/testscheduledb.json')