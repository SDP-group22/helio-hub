import pytest
import json
from mock import patch
from tinydb import TinyDB

"""NOTE: the order of tests is important!!!"""

@patch('motion-sensor.db', TinyDB('./database/testmotiondb.json'))
def test_get_returns_404(motion_db, client):
    response = client.get('/motion/99')
    
    assert response.status_code == 404

@patch('motion-sensor.db', TinyDB('./database/testmotiondb.json'))
def test_get_returns_motion_object(motion_db, motion_object, client):
    response = client.get('/motion/0')
    
    assert response.json == motion_object

@patch('motion-sensor.db', TinyDB('./database/testmotiondb.json'))
def test_get_returns_200(motion_db, client):
    response = client.get('/motion/0')
    
    assert response.status_code == 200

@patch('motion-sensor.db', TinyDB('./database/testmotiondb.json'))
def test_get_all_returns_200(motion_db, client):
    response = client.get('/motion/get_all')
    
    assert response.status_code == 200

@patch('motion-sensor.db', TinyDB('./database/testmotiondb.json'))
@patch('motion-sensor.motor_db', TinyDB('./database/testmotordb.json'))
def test_register_returns_200(motion_db, motor_db, motion_object, client):

    response = client.post('/motion/register',
                        data=json.dumps(motion_object),
                        content_type='application/json')

    assert response.status_code == 200

@patch('motion-sensor.db', TinyDB('./database/testmotiondb.json'))
@patch('motion-sensor.motor_db', TinyDB('./database/testmotordb.json'))
def test_register_increments_motion_id(motion_db, motor_db, motion_object, client):
    response = client.post('/motion/register',
                        data=json.dumps(motion_object),
                        content_type='application/json')
    
    assert response.json['id'] == 2

@patch('motion-sensor.db', TinyDB('./database/testmotiondb.json'))
@patch('motion-sensor.motor_db', TinyDB('./database/testmotordb.json'))
def test_register_returns_400_when_invalid_motor(motion_db, motion_object, client):
    motion_object['motor_ids'] = [2000]

    response = client.post('/motion/register',
                        data=json.dumps(motion_object),
                        content_type='application/json')
    
    assert response.status_code == 400

@patch('motion-sensor.db', TinyDB('./database/testmotiondb.json'))
def test_unregister_returns_200_when_motion_found(motion_db, client):
    response = client.delete('/motion/unregister/1')
    
    assert response.status_code == 200

@patch('motion-sensor.db', TinyDB('./database/testmotiondb.json'))
def test_unregister_returns_404_when_motion_not_found(motion_db, client):
    response = client.delete('/motion/unregister/1')
    
    assert response.status_code == 404

@patch('motion-sensor.motor_db', TinyDB('./database/testmotordb.json'))
@patch('motion-sensor.db', TinyDB('./database/testmotiondb.json'))
def test_update_returns_200_when_motion_found(motion_db, motor_db, motion_object, client):
    
    response = client.patch('/motion/update/0',
                        data=json.dumps(motion_object),
                        content_type='application/json')
    
    assert response.status_code == 200

@patch('motion-sensor.db', TinyDB('./database/testmotiondb.json'))
def test_update_returns_400_when_invalid_motor(motion_object, client):
    motion_object['motor_ids'] = [2000]

    response = client.patch('/motion/update/0',
                        data=json.dumps(motion_object),
                        content_type='application/json')
    
    assert response.status_code == 400

@patch('motion-sensor.motor_db', TinyDB('./database/testmotordb.json'))
@patch('motion-sensor.db', TinyDB('./database/testmotiondb.json'))
def test_update_returns_404_when_motion_not_found(motor_db, motion_object, client):
    
    response = client.patch('/motion/update/99',
                        data=json.dumps(motion_object),
                        content_type='application/json')
    
    assert response.status_code == 404

@patch('motion-sensor.db', TinyDB('./database/testmotiondb.json'))
def test_deactivate_returns_200_when_motion_found(motion_db, client):
    response = client.patch('/motion/deactivate/0')

    assert response.status_code == 200

@patch('motion-sensor.db', TinyDB('./database/testmotiondb.json'))
def test_deactivate_returns_404_when_motion_not_found(motion_db, client):
    response = client.patch('/motion/deactivate/99')

    assert response.status_code == 404