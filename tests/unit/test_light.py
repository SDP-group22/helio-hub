import pytest
import json
from mock import patch
from tinydb import TinyDB, Query
import os
import time

"""NOTE: the order of tests is important!!!"""

@patch('light-sensor.db', TinyDB('./database/testlightdb.json'))
def test_get_returns_404(light_db, client):
    response = client.get('/light/1')
    
    assert response.status_code == 404

@patch('light-sensor.db', TinyDB('./database/testlightdb.json'))
def test_get_returns_light_object(light_db, light_object, client):
    response = client.get('/light/0')
    
    assert response.json == light_object

@patch('light-sensor.db', TinyDB('./database/testlightdb.json'))
def test_get_returns_200(light_db, client):
    response = client.get('/light/0')
    
    assert response.status_code == 200

@patch('light-sensor.db', TinyDB('./database/testlightdb.json'))
def test_get_all_returns_empty_list(light_db, light_object, client):

    # remove dummy record
    response = client.get('/light/get_all')
    
    assert response.json == [light_object]

@patch('light-sensor.db', TinyDB('./database/testlightdb.json'))
def test_get_all_returns_200(light_db, client):
    response = client.get('/light/get_all')
    
    assert response.status_code == 200

@patch('light-sensor.db', TinyDB('./database/testlightdb.json'))
@patch('light-sensor.motor_db', TinyDB('./database/testmotordb.json'))
def test_register_returns_200(light_db, motor_db, light_object, client):

    response = client.post('/light/register',
                        data=json.dumps(light_object),
                        content_type='application/json')

    assert response.status_code == 200

@patch('light-sensor.db', TinyDB('./database/testlightdb.json'))
@patch('light-sensor.motor_db', TinyDB('./database/testmotordb.json'))
def test_register_increments_light_id(light_db, motor_db, light_object, client):
    response = client.post('/light/register',
                        data=json.dumps(light_object),
                        content_type='application/json')
    
    assert response.json['id'] == 2

@patch('light-sensor.db', TinyDB('./database/testlightdb.json'))
@patch('light-sensor.motor_db', TinyDB('./database/testmotordb.json'))
def test_register_returns_400_when_invalid_motor(light_db, light_object, client):
    light_object['motor_ids'] = [2000]

    response = client.post('/light/register',
                        data=json.dumps(light_object),
                        content_type='application/json')
    
    assert response.status_code == 400

@patch('light-sensor.db', TinyDB('./database/testlightdb.json'))
def test_unregister_returns_200_when_light_found(light_db, client):
    response = client.delete('/light/unregister/1')
    
    assert response.status_code == 200

@patch('light-sensor.db', TinyDB('./database/testlightdb.json'))
def test_unregister_returns_404_when_light_not_found(light_db, client):
    response = client.delete('/light/unregister/1')
    
    assert response.status_code == 404

@patch('light-sensor.motor_db', TinyDB('./database/testmotordb.json'))
@patch('light-sensor.db', TinyDB('./database/testlightdb.json'))
def test_update_returns_200_when_light_found(light_db, motor_db, light_object, client):
    
    response = client.patch('/light/update/0',
                        data=json.dumps(light_object),
                        content_type='application/json')
    
    assert response.status_code == 200

@patch('light-sensor.db', TinyDB('./database/testlightdb.json'))
def test_update_returns_400_when_invalid_motor(light_object, client):
    light_object['motor_ids'] = [2000]

    response = client.patch('/light/update/0',
                        data=json.dumps(light_object),
                        content_type='application/json')
    
    assert response.status_code == 400

@patch('light-sensor.motor_db', TinyDB('./database/testmotordb.json'))
@patch('light-sensor.db', TinyDB('./database/testlightdb.json'))
def test_update_returns_404_when_light_not_found(motor_db, light_object, client):
    
    response = client.patch('/light/update/99',
                        data=json.dumps(light_object),
                        content_type='application/json')
    
    assert response.status_code == 404

@patch('light-sensor.db', TinyDB('./database/testlightdb.json'))
def test_deactivate_returns_200_when_light_found(light_db, client):
    response = client.patch('/light/deactivate/0')

    assert response.status_code == 200

@patch('light-sensor.db', TinyDB('./database/testlightdb.json'))
def test_deactivate_returns_404_when_light_not_found(light_db, client):
    response = client.patch('/light/deactivate/99')

    assert response.status_code == 404