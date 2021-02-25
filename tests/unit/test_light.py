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
    os.remove('./database/testdb.json')

@pytest.fixture(scope='module')
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

"""NOTE: the order of tests is important!!!"""

@patch('light-sensor.db', TinyDB('./database/testdb.json'))
def test_get_returns_400(light_object, client):
    response = client.get('/light/0')
    
    assert response.status_code == 400

@patch('light-sensor.db', TinyDB('./database/testdb.json'))
def test_get_all_returns_empty_list(light_object, client):
    response = client.get('/light/get_all')
    
    assert response.json == []

@patch('light-sensor.db', TinyDB('./database/testdb.json'))
def test_get_all_returns_200_when_db_empty(light_object, client):
    response = client.get('/light/get_all')
    
    assert response.status_code == 200

@patch('light-sensor.db', TinyDB('./database/testdb.json'))
def test_register_returns_200(light_object, client):
    response = client.post('/light/register',
                        data=json.dumps(light_object),
                        content_type='application/json')

    assert response.status_code == 200

@patch('light-sensor.db', TinyDB('./database/testdb.json'))
def test_get_returns_200(light_object, client):
    response = client.get('/light/0')
    
    assert response.status_code == 200

@patch('light-sensor.db', TinyDB('./database/testdb.json'))
def test_get_returns_light_object(light_object, client):
    response = client.get('/light/0')
    
    assert response.json == light_object

@patch('light-sensor.db', TinyDB('./database/testdb.json'))
def test_get_all_returns_light_in_list(light_object, client):
    response = client.get('/light/get_all')
    
    assert response.json == [light_object]

@patch('light-sensor.db', TinyDB('./database/testdb.json'))
def test_register_increments_light_id(light_object, client):
    response = client.post('/light/register',
                        data=json.dumps(light_object),
                        content_type='application/json')
    
    assert response.json['id'] == 1

@patch('light-sensor.db', TinyDB('./database/testdb.json'))
def test_register_returns_400_when_invalid_motor(light_object, client):
    light_object['motor_ids'] = [2000]

    response = client.post('/light/register',
                        data=json.dumps(light_object),
                        content_type='application/json')
    
    assert response.status_code == 400

@patch('light-sensor.db', TinyDB('./database/testdb.json'))
def test_unregister_returns_200_when_light_found(light_object, client):
    response = client.delete('/light/unregister/1')
    
    assert response.status_code == 200

@patch('light-sensor.db', TinyDB('./database/testdb.json'))
def test_unregister_returns_400_when_light_not_found(light_object, client):
    response = client.delete('/light/unregister/1')
    
    assert response.status_code == 400

@patch('light-sensor.db', TinyDB('./database/testdb.json'))
def test_update_returns_200_when_light_found(light_object, client):
    
    response = client.patch('/light/update/0',
                        data=json.dumps(light_object),
                        content_type='application/json')
    
    assert response.status_code == 200

@patch('light-sensor.db', TinyDB('./database/testdb.json'))
def test_update_updates_name(light_object, client):
    
    update_content = {'name': 'updated'}

    response = client.patch('/light/update/0',
                        data=json.dumps(update_content),
                        content_type='application/json')
    
    assert response.json['name'] == 'updated'

@patch('light-sensor.db', TinyDB('./database/testdb.json'))
def test_update_returns_400_when_invalid_motor(light_object, client):
    light_object['motor_ids'] = [2000]

    response = client.patch('/light/update/0',
                        data=json.dumps(light_object),
                        content_type='application/json')
    
    assert response.status_code == 400

@patch('light-sensor.db', TinyDB('./database/testdb.json'))
def test_update_returns_400_when_light_not_found(light_object, client):
    
    update_content = {'name': 'updated'}

    response = client.patch('/light/update/99',
                        data=json.dumps(update_content),
                        content_type='application/json')
    
    assert response.status_code == 400

@patch('light-sensor.db', TinyDB('./database/testdb.json'))
def test_deactivate_returns_200_when_light_found(light_object, client):
    response = client.patch('/light/deactivate/0')

    assert response.status_code == 200

@patch('light-sensor.db', TinyDB('./database/testdb.json'))
def test_deactivate_returns_400_when_light_not_found(light_object, client):
    response = client.patch('/light/deactivate/99')

    assert response.status_code == 400

# @pytest.mark.skip(reason='Teardown function')
# def test_teardown():
#     os.remove('./database/testdb.json')