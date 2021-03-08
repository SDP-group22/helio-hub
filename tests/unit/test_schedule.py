import pytest
import json
from mock import patch
from tinydb import TinyDB

"""NOTE: the order of tests is important!!!"""

@patch('schedule.db', TinyDB('./database/testscheduledb.json'))
def test_get_returns_404(schedule_db, client):
    response = client.get('/schedule/1')
    
    assert response.status_code == 404

@patch('schedule.db', TinyDB('./database/testscheduledb.json'))
def test_get_returns_schedule_object(schedule_db, schedule_object, client):
    response = client.get('/schedule/0')
    
    assert response.json == schedule_object

@patch('motor.db', TinyDB('./database/testmotordb.json'))
def test_get_returns_200(motor_db, client):
    response = client.get('/motor/0')
    
    assert response.status_code == 200

@patch('schedule.db', TinyDB('./database/testscheduledb.json'))
def test_get_all_returns_empty_list(schedule_db, schedule_object, client):

    response = client.get('/schedule/get_all')
    
    assert response.json == [schedule_object]

@patch('schedule.db', TinyDB('./database/testscheduledb.json'))
def test_get_all_returns_200(schedule_db, client):
    response = client.get('/schedule/get_all')
    
    assert response.status_code == 200

@patch('schedule.db', TinyDB('./database/testscheduledb.json'))
@patch('schedule.motor_db', TinyDB('./database/testmotordb.json'))
def test_register_returns_200(schedule_db, motor_db, schedule_object, client):

    response = client.post('/schedule/register',
                        data=json.dumps(schedule_object),
                        content_type='application/json')

    assert response.status_code == 200

@patch('schedule.db', TinyDB('./database/testscheduledb.json'))
@patch('schedule.motor_db', TinyDB('./database/testmotordb.json'))
def test_register_increments_schedule_id(schedule_db, motor_db, schedule_object, client):
    response = client.post('/schedule/register',
                        data=json.dumps(schedule_object),
                        content_type='application/json')
    
    assert response.json['id'] == 2

@patch('schedule.db', TinyDB('./database/testscheduledb.json'))
@patch('schedule.motor_db', TinyDB('./database/testmotordb.json'))
def test_register_returns_400_when_invalid_motor(schedule_db, schedule_object, client):
    schedule_object['motor_ids'] = [2000]

    response = client.post('/schedule/register',
                        data=json.dumps(schedule_object),
                        content_type='application/json')
    
    assert response.status_code == 400

@patch('schedule.db', TinyDB('./database/testscheduledb.json'))
def test_unregister_returns_200_when_schedule_found(schedule_db, client):
    response = client.delete('/schedule/unregister/1')
    
    assert response.status_code == 200

@patch('schedule.db', TinyDB('./database/testscheduledb.json'))
def test_unregister_returns_404_when_schedule_not_found(schedule_db, client):
    response = client.delete('/schedule/unregister/1')
    
    assert response.status_code == 404

@patch('schedule.motor_db', TinyDB('./database/testmotordb.json'))
@patch('schedule.db', TinyDB('./database/testscheduledb.json'))
def test_update_returns_200_when_schedule_found(schedule_db, motor_db, schedule_object, client):
    
    response = client.patch('/schedule/update/0',
                        data=json.dumps(schedule_object),
                        content_type='application/json')
    
    assert response.status_code == 200

@patch('schedule.db', TinyDB('./database/testscheduledb.json'))
def test_update_returns_400_when_invalid_motor(schedule_object, client):
    schedule_object['motor_ids'] = [2000]

    response = client.patch('/schedule/update/0',
                        data=json.dumps(schedule_object),
                        content_type='application/json')
    
    assert response.status_code == 400

@patch('schedule.motor_db', TinyDB('./database/testmotordb.json'))
@patch('schedule.db', TinyDB('./database/testscheduledb.json'))
def test_update_returns_404_when_schedule_not_found(motor_db, schedule_object, client):
    
    response = client.patch('/schedule/update/99',
                        data=json.dumps(schedule_object),
                        content_type='application/json')
    
    assert response.status_code == 404

@patch('schedule.db', TinyDB('./database/testscheduledb.json'))
def test_deactivate_returns_200_when_schedule_found(schedule_db, client):
    response = client.patch('/schedule/deactivate/0')

    assert response.status_code == 200

@patch('schedule.db', TinyDB('./database/testscheduledb.json'))
def test_deactivate_returns_404_when_schedule_not_found(schedule_db, client):
    response = client.patch('/schedule/deactivate/99')

    assert response.status_code == 404