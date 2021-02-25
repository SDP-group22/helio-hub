from api import get_app
import pytest
import json
from mock import patch
from tinydb import TinyDB
import os

@pytest.fixture(scope="module")
def client():
    with get_app().app.test_client() as c:
        yield c
    
    # teardown
    os.remove('./database/testmotiondb.json')

@pytest.fixture(scope='module')
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

"""NOTE: the order of tests is important!!!"""

@patch('motion-sensor.db', TinyDB('./database/testmotiondb.json'))
def test_get_returns_400(motion_object, client):
    response = client.get('/motion/0')
    
    assert response.status_code == 400

@patch('motion-sensor.db', TinyDB('./database/testmotiondb.json'))
def test_get_all_returns_empty_list(motion_object, client):
    response = client.get('/motion/get_all')
    
    assert response.json == []

@patch('motion-sensor.db', TinyDB('./database/testmotiondb.json'))
def test_get_all_returns_200_when_db_empty(motion_object, client):
    response = client.get('/motion/get_all')
    
    assert response.status_code == 200

@patch('motion-sensor.db', TinyDB('./database/testmotiondb.json'))
def test_register_returns_200(motion_object, client):
    response = client.post('/motion/register',
                        data=json.dumps(motion_object),
                        content_type='application/json')

    assert response.status_code == 200

@patch('motion-sensor.db', TinyDB('./database/testmotiondb.json'))
def test_get_returns_200(motion_object, client):
    response = client.get('/motion/0')
    
    assert response.status_code == 200

@patch('motion-sensor.db', TinyDB('./database/testmotiondb.json'))
def test_get_returns_motion_object(motion_object, client):
    response = client.get('/motion/0')
    
    assert response.json == motion_object

@patch('motion-sensor.db', TinyDB('./database/testmotiondb.json'))
def test_get_all_returns_motion_in_list(motion_object, client):
    response = client.get('/motion/get_all')
    
    assert response.json == [motion_object]

@patch('motion-sensor.db', TinyDB('./database/testmotiondb.json'))
def test_register_increments_motion_id(motion_object, client):
    response = client.post('/motion/register',
                        data=json.dumps(motion_object),
                        content_type='application/json')
    
    assert response.json['id'] == 1

@patch('motion-sensor.db', TinyDB('./database/testmotiondb.json'))
def test_register_returns_400_when_invalid_motor(motion_object, client):
    motion_object['motor_ids'] = [2000]

    response = client.post('/motion/register',
                        data=json.dumps(motion_object),
                        content_type='application/json')
    
    assert response.status_code == 400

@patch('motion-sensor.db', TinyDB('./database/testmotiondb.json'))
def test_unregister_returns_200_when_motion_found(motion_object, client):
    response = client.delete('/motion/unregister/1')
    
    assert response.status_code == 200

@patch('motion-sensor.db', TinyDB('./database/testmotiondb.json'))
def test_unregister_returns_400_when_motion_not_found(motion_object, client):
    response = client.delete('/motion/unregister/1')
    
    assert response.status_code == 400

@patch('motion-sensor.db', TinyDB('./database/testmotiondb.json'))
def test_update_returns_200_when_motion_found(motion_object, client):
    
    response = client.patch('/motion/update/0',
                        data=json.dumps(motion_object),
                        content_type='application/json')
    
    assert response.status_code == 200

@patch('motion-sensor.db', TinyDB('./database/testmotiondb.json'))
def test_update_updates_name(motion_object, client):
    
    update_content = {'name': 'updated'}

    response = client.patch('/motion/update/0',
                        data=json.dumps(update_content),
                        content_type='application/json')
    
    assert response.json['name'] == 'updated'

@patch('motion-sensor.db', TinyDB('./database/testmotiondb.json'))
def test_update_returns_400_when_invalid_motor(motion_object, client):
    motion_object['motor_ids'] = [2000]

    response = client.patch('/motion/update/0',
                        data=json.dumps(motion_object),
                        content_type='application/json')
    
    assert response.status_code == 400

@patch('motion-sensor.db', TinyDB('./database/testmotiondb.json'))
def test_update_returns_400_when_motion_not_found(motion_object, client):
    
    update_content = {'name': 'updated'}

    response = client.patch('/motion/update/99',
                        data=json.dumps(update_content),
                        content_type='application/json')
    
    assert response.status_code == 400

@patch('motion-sensor.db', TinyDB('./database/testmotiondb.json'))
def test_deactivate_returns_200_when_motion_found(motion_object, client):
    response = client.patch('/motion/deactivate/0')

    assert response.status_code == 200

@patch('motion-sensor.db', TinyDB('./database/testmotiondb.json'))
def test_deactivate_returns_400_when_motion_not_found(motion_object, client):
    response = client.patch('/motion/deactivate/99')

    assert response.status_code == 400

# @pytest.mark.skip(reason='Teardown function')
# def test_teardown():
#     os.remove('./database/testmotiondb.json')