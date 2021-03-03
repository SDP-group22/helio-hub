import pytest
import json
from mock import patch
from tinydb import TinyDB

"""NOTE: the order of tests is important!!!"""

@patch('motor.db', TinyDB('./database/testmotordb.json'))
def test_get_returns_404(motor_db, client):
    response = client.get('/motor/99')
    
    assert response.status_code == 404

@patch('motor.db', TinyDB('./database/testmotordb.json'))
def test_get_returns_motor_object(motor_db, motor_object, client):
    response = client.get('/motor/0')
    
    assert response.json == motor_object

@patch('motor.db', TinyDB('./database/testmotordb.json'))
def test_get_returns_200(motor_db, client):
    response = client.get('/motor/0')
    
    assert response.status_code == 200

@patch('motor.db', TinyDB('./database/testmotordb.json'))
def test_get_all_returns_empty_list(motor_db, motor_object, client):

    response = client.get('/motor/get_all')
    
    assert response.json == [motor_object]

@patch('motor.db', TinyDB('./database/testmotordb.json'))
def test_get_all_returns_200(motor_db, client):
    response = client.get('/motor/get_all')
    
    assert response.status_code == 200

@patch('motor.db', TinyDB('./database/testmotordb.json'))
def test_register_returns_200(motor_db, motor_object, client):

    response = client.post('/motor/register',
                        data=json.dumps(motor_object),
                        content_type='application/json')

    assert response.status_code == 200

@patch('motor.db', TinyDB('./database/testmotordb.json'))
def test_register_increments_motor_id(motor_db, motor_object, client):
    response = client.post('/motor/register',
                        data=json.dumps(motor_object),
                        content_type='application/json')
    
    assert response.json['id'] == 2

@patch('motor.db', TinyDB('./database/testmotordb.json'))
def test_unregister_returns_200_when_motor_found(motor_db, client):
    response = client.delete('/motor/unregister/1')
    
    assert response.status_code == 200

@patch('motor.db', TinyDB('./database/testmotordb.json'))
def test_unregister_returns_404_when_motor_not_found(motor_db, client):
    response = client.delete('/motor/unregister/1')
    
    assert response.status_code == 404

@patch('motor.db', TinyDB('./database/testmotordb.json'))
def test_update_returns_200_when_motor_found(motor_db, motor_object, client):
    
    response = client.patch('/motor/update/0',
                        data=json.dumps(motor_object),
                        content_type='application/json')
    
    assert response.status_code == 200

@patch('motor.db', TinyDB('./database/testmotordb.json'))
def test_update_returns_404_when_motor_not_found(motor_db, motor_object, client):
    
    response = client.patch('/motor/update/99',
                        data=json.dumps(motor_object),
                        content_type='application/json')
    
    assert response.status_code == 404

@patch('motor.db', TinyDB('./database/testmotordb.json'))
def test_deactivate_returns_200_when_motor_found(motor_db, client):
    response = client.patch('/motor/deactivate/0')

    assert response.status_code == 200

@patch('motor.db', TinyDB('./database/testmotordb.json'))
def test_deactivate_returns_404_when_motor_not_found(motor_db, client):
    response = client.patch('/motor/deactivate/99')

    assert response.status_code == 404