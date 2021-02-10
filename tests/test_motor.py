from api import get_app
import pytest
import json
from mock import patch

@pytest.fixture(scope="module")
def client():
    with get_app().app.test_client() as c:
        yield c

@pytest.fixture(scope='module')
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

@patch('motor.db')
def test_get_returns_motor_object(mock_db, motor_object, client):
    mock_db.search.return_value = [motor_object]

    response = client.get('/motor/0')

    mock_db.search.assert_called_once()
    assert response.status_code == 200
    assert response.json == motor_object

@patch('motor.db')
def test_get_returns_not_found(mock_db, client):
    mock_db.search.return_value = [None]

    response = client.get('/motor/0')

    mock_db.search.assert_called_once()
    assert response.status_code == 400

@patch('motor.db')
def test_get_catches_exception(mock_db, client):
    mock_db.search.side_effect = Exception

    response = client.get('/motor/0')
    assert response.status_code == 500

@patch('motor.db')
def test_get_all_catches_exception(mock_db, client):
    mock_db.search.side_effect = Exception

    response = client.get('/motor/get_all')

    assert response.status_code == 500

@patch('motor.db')
def test_get_all_returns_200_when_db_empty(mock_db, client):
    mock_db.all.return_value = []

    response = client.get('/motor/get_all')

    assert response.json == []
    assert response.status_code == 200

@patch('motor.db')
def test_get_all_returns_200_when_db_not_empty(mock_db, motor_object, client):
    mock_db.all.return_value = [motor_object, motor_object]

    response = client.get('/motor/get_all')

    assert response.json == [motor_object, motor_object]
    assert response.status_code == 200

@patch('motor.db')
def test_get_all_returns_200_when_db_not_empty(mock_db, motor_object, client):
    mock_db.all.return_value = [motor_object, motor_object]

    response = client.get('/motor/get_all')

    assert response.json == [motor_object, motor_object]
    assert response.status_code == 200

@patch('motor.db')
def test_register_increments_id(mock_db, motor_object, client):
    mock_db.all.return_value = [{'id':88}]

    response = client.post('/motor/register',
                        data=json.dumps(motor_object),
                        content_type='application/json')

    motor_object['id'] = 89

    mock_db.insert.assert_called_once_with(motor_object)

@patch('motor.db')
def test_register_starts_id_at_0(mock_db, motor_object, client):
    mock_db.search.return_value = []

    response = client.post('/motor/register',
                        data=json.dumps(motor_object),
                        content_type='application/json')
    
    motor_object['id'] = 0

    mock_db.insert.assert_called_once_with(motor_object)

@patch('motor.db')
def test_register_catches_exception(mock_db, motor_object, client):
    mock_db.search.side_effect = Exception

    response = client.post('/motor/register',
                        data=json.dumps(motor_object),
                        content_type='application/json')

    assert response.status_code == 500

@patch('motor.db')
def test_unregister_returns_200_when_motor_found(mock_db, motor_object, client):
    mock_db.search.return_value = [motor_object]

    response = client.delete('/motor/unregister/1')

    assert response.status_code == 200

@patch('motor.db')
def test_unregister_returns_400_when_motor_not_found(mock_db, client):
    mock_db.search.return_value = []

    response = client.delete('/motor/unregister/1')

    assert response.status_code == 400

@patch('motor.db')
def test_unregister_catches_exception(mock_db, client):
    mock_db.search.side_effect = Exception

    response = client.delete('/motor/unregister/1')

    assert response.status_code == 500

@patch('motor.db')
def test_move_returns_200_when_motor_found(mock_db, motor_object, client):
    mock_db.search.return_value = [motor_object]
    mock_db.get.return_value = motor_object

    response = client.patch('/motor/move',
                        data=json.dumps(motor_object),
                        content_type='application/json')

    assert response.status_code == 200

@patch('motor.db')
def test_move_returns_400_when_motor_not_found(mock_db, motor_object, client):
    mock_db.search.return_value = []

    response = client.patch('/motor/move',
                        data=json.dumps(motor_object),
                        content_type='application/json')

    assert response.status_code == 400

@patch('motor.db')
def test_move_catches_exception(mock_db, motor_object, client):
    mock_db.search.side_effect = Exception

    response = client.patch('/motor/move',
                        data=json.dumps(motor_object),
                        content_type='application/json')

    assert response.status_code == 500

@patch('motor.db')
def test_rename_returns_200_when_motor_found(mock_db, motor_object, client):
    mock_db.search.return_value = [motor_object]
    mock_db.get.return_value = motor_object

    response = client.patch('/motor/rename',
                        data=json.dumps(motor_object),
                        content_type='application/json')

    assert response.status_code == 200

@patch('motor.db')
def test_rename_returns_400_when_motor_not_found(mock_db, motor_object, client):
    mock_db.search.return_value = []

    response = client.patch('/motor/rename',
                        data=json.dumps(motor_object),
                        content_type='application/json')

    assert response.status_code == 400

@patch('motor.db')
def test_rename_catches_exception(mock_db, motor_object, client):
    mock_db.search.side_effect = Exception

    response = client.patch('/motor/rename',
                        data=json.dumps(motor_object),
                        content_type='application/json')

    assert response.status_code == 500

@patch('motor.db')
def test_deactivate_returns_200_when_motor_found(mock_db, motor_object, client):
    mock_db.search.return_value = [motor_object]
    mock_db.get.return_value = motor_object

    response = client.patch('/motor/deactivate/1')

    assert response.status_code == 200

@patch('motor.db')
def test_deactivate_returns_400_when_motor_not_found(mock_db, client):
    mock_db.search.return_value = []

    response = client.patch('/motor/deactivate/1')

    assert response.status_code == 400

@patch('motor.db')
def test_deactivate_catches_exception(mock_db, client):
    mock_db.search.side_effect = Exception

    response = client.patch('/motor/deactivate/1')

    assert response.status_code == 500

@patch('motor.db')
def test_activate_returns_200_when_motor_found(mock_db, motor_object, client):
    mock_db.search.return_value = [motor_object]
    mock_db.get.return_value = motor_object

    response = client.patch('/motor/activate/1')

    assert response.status_code == 200

@patch('motor.db')
def test_activate_returns_400_when_motor_not_found(mock_db, client):
    mock_db.search.return_value = []

    response = client.patch('/motor/activate/1')

    assert response.status_code == 400

@patch('motor.db')
def test_activate_catches_exception(mock_db, client):
    mock_db.search.side_effect = Exception

    response = client.patch('/motor/activate/1')

    assert response.status_code == 500



