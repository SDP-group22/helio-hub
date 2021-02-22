from api import get_app
import pytest
import json
from datetime import datetime
from mock import patch

@pytest.fixture(scope="module")
def client():
    with get_app().app.test_client() as c:
        yield c

@pytest.fixture(scope='module')
def schedule_object():
    schedule_object = {}
    schedule_object['id'] = 0
    schedule_object['name'] = 'test_motor'
    schedule_object['active'] = False
    schedule_object['gradient'] = 30
    schedule_object['target-level'] = 50
    schedule_object['time'] = '07:00'
    schedule_object['days'] = ['Monday', 'Tuesday']
    schedule_object['motor-ids'] = [2]

    return schedule_object

# @patch('shedule.schedule_table')
# def test_get_returns_schedule_object(mock_db, schedule_object, client):
#     mock_db.search.return_value = [schedule_object]

#     response = client.get('schedule/get/0')

#     mock_db.search.assert_called_once()
#     assert response.status_code == 200
#     assert response.json == schedule_object

# @patch('shedule.schedule_table')
# def test_get_returns_not_found(mock_db, client):
#     mock_db.search.return_value = None

#     response = client.get('schedule/get/0')

#     mock_db.search.assert_called_once()
#     assert response.status_code == 400

# @patch('shedule.schedule_table')
# def test_get_catches_exception(mock_db, client):
#     mock_db.search.side_effect = Exception

#     response = client.get('schedule/get/0')

#     assert response.status_code == 500

# @patch('shedule.schedule_table')
# def test_get_all_catches_exception(mock_db, client):
#     mock_db.search.side_effect = Exception

#     response = client.get('/schedule/get_all')

#     assert response.status_code == 500

# @patch('shedule.schedule_table')
# def test_get_all_returns_200_when_db_empty(mock_db, client):
#     mock_db.all.return_value = []

#     response = client.get('/schedule/get_all')

#     assert response.json == []
#     assert response.status_code == 200

# @patch('shedule.schedule_table')
# def test_get_all_returns_200_when_db_not_empty(mock_db, schedule_object, client):
#     mock_db.all.return_value = [schedule_object, schedule_object]

#     response = client.get('/schedule/get_all')

#     assert response.json == [schedule_object, schedule_object]
#     assert response.status_code == 200

@patch('shedule.datetime')
@patch('shedule.schedule_table')
@patch('motor.motor_table')
def test_register_increments_id(mock_motor_table, 
    mock_schedule_table,
    mock_dt,
    schedule_object, 
    client):
    mock_motor_table.search.return_value = True
    mock_schedule_table.all.return_value = [{'id':88,'last_modified':None}]
    mock_schedule_table.search.return_value = [{'id':88,'last_modified':None}]
    mock_dt.now.return_value = None

    response = client.post('/schedule/register',
                        data=json.dumps(schedule_object),
                        content_type='application/json')

    schedule_object['id'] = 89
    schedule_object['last_modified'] = 'None'

    mock_schedule_table.insert.assert_called_once_with(schedule_object)

@patch('shedule.datetime')
@patch('shedule.schedule_table')
@patch('motor.motor_table')
def test_register_starts_id_at_0(mock_motor_table, 
    mock_schedule_table,
    mock_dt,
    schedule_object, 
    client):

    mock_motor_table.search.return_value = True
    mock_schedule_table.all.return_value = []
    mock_schedule_table.search.return_value = []
    mock_dt.now.return_value = None

    response = client.post('/schedule/register',
                        data=json.dumps(schedule_object),
                        content_type='application/json')
    
    schedule_object['id'] = 0
    schedule_object['last_modified'] = 'None'

    mock_schedule_table.insert.assert_called_once_with(schedule_object)

@patch('shedule.schedule_table')
def test_register_catches_exception(mock_db, schedule_object, client):
    mock_db.search.side_effect = Exception

    response = client.post('/schedule/register',
                        data=json.dumps(schedule_object),
                        content_type='application/json')

    assert response.status_code == 500

@patch('shedule.schedule_table')
def test_unregister_returns_200_when_motor_found(mock_db, schedule_object, client):
    mock_db.search.return_value = [schedule_object]

    response = client.delete('/schedule/unregister/1')

    assert response.status_code == 200

@patch('shedule.schedule_table')
def test_unregister_returns_400_when_motor_not_found(mock_db, client):
    mock_db.search.return_value = []

    response = client.delete('/schedule/unregister/1')

    assert response.status_code == 400

@patch('shedule.schedule_table')
def test_unregister_catches_exception(mock_db, client):
    mock_db.search.side_effect = Exception

    response = client.delete('/schedule/unregister/1')

    assert response.status_code == 500

@patch('shedule.schedule_table')
def test_change_days_returns_200_when_schedule_found(mock_db, schedule_object, client):
    mock_db.search.return_value = [schedule_object]
    mock_db.get.return_value = schedule_object

    response = client.patch('/schedule/change_days',
                        data=json.dumps(schedule_object),
                        content_type='application/json')

    assert response.status_code == 200

@patch('shedule.schedule_table')
def test_change_days_returns_400_when_schedule_not_found(mock_db, schedule_object, client):
    mock_db.search.return_value = []

    response = client.patch('/schedule/change_days',
                        data=json.dumps(schedule_object),
                        content_type='application/json')

    assert response.status_code == 400

@patch('shedule.schedule_table')
def test_change_days_catches_exception(mock_db, schedule_object, client):
    mock_db.search.side_effect = Exception

    response = client.patch('/schedule/change_days',
                        data=json.dumps(schedule_object),
                        content_type='application/json')

    assert response.status_code == 500

@patch('shedule.schedule_table')
def test_change_time_returns_200_when_schedule_found(mock_db, schedule_object, client):
    mock_db.search.return_value = [schedule_object]
    mock_db.get.return_value = schedule_object

    response = client.patch('/schedule/change_time',
                        data=json.dumps(schedule_object),
                        content_type='application/json')

    assert response.status_code == 200

@patch('shedule.schedule_table')
def test_change_time_returns_400_when_schedule_not_found(mock_db, schedule_object, client):
    mock_db.search.return_value = []

    response = client.patch('/schedule/change_time',
                        data=json.dumps(schedule_object),
                        content_type='application/json')

    assert response.status_code == 400

@patch('shedule.schedule_table')
def test_change_time_catches_exception(mock_db, schedule_object, client):
    mock_db.search.side_effect = Exception

    response = client.patch('/schedule/change_time',
                        data=json.dumps(schedule_object),
                        content_type='application/json')

    assert response.status_code == 500

@patch('shedule.schedule_table')
def test_change_gradient_returns_200_when_schedule_found(mock_db, schedule_object, client):
    mock_db.search.return_value = [schedule_object]
    mock_db.get.return_value = schedule_object

    response = client.patch('/schedule/change_gradient',
                        data=json.dumps(schedule_object),
                        content_type='application/json')

    assert response.status_code == 200

@patch('shedule.schedule_table')
def test_change_gradient_returns_400_when_schedule_not_found(mock_db, schedule_object, client):
    mock_db.search.return_value = []

    response = client.patch('/schedule/change_gradient',
                        data=json.dumps(schedule_object),
                        content_type='application/json')

    assert response.status_code == 400

@patch('shedule.schedule_table')
def test_change_gradient_catches_exception(mock_db, schedule_object, client):
    mock_db.search.side_effect = Exception

    response = client.patch('/schedule/change_gradient',
                        data=json.dumps(schedule_object),
                        content_type='application/json')

    assert response.status_code == 500

@patch('shedule.schedule_table')
def test_rename_returns_200_when_motor_found(mock_db, schedule_object, client):
    mock_db.search.return_value = [schedule_object]
    mock_db.get.return_value = schedule_object

    response = client.patch('/schedule/rename',
                        data=json.dumps(schedule_object),
                        content_type='application/json')

    assert response.status_code == 200

@patch('shedule.schedule_table')
def test_rename_returns_400_when_motor_not_found(mock_db, schedule_object, client):
    mock_db.search.return_value = []

    response = client.patch('/schedule/rename',
                        data=json.dumps(schedule_object),
                        content_type='application/json')

    assert response.status_code == 400

@patch('shedule.schedule_table')
def test_rename_catches_exception(mock_db, schedule_object, client):
    mock_db.search.side_effect = Exception

    response = client.patch('/schedule/rename',
                        data=json.dumps(schedule_object),
                        content_type='application/json')

    assert response.status_code == 500

@patch('shedule.schedule_table')
def test_deactivate_returns_200_when_schedule_found(mock_db, schedule_object, client):
    mock_db.search.return_value = [schedule_object]
    mock_db.get.return_value = schedule_object

    response = client.patch('/schedule/deactivate/1')

    assert response.status_code == 200

@patch('shedule.schedule_table')
def test_deactivate_returns_400_when_schedule_not_found(mock_db, client):
    mock_db.search.return_value = []

    response = client.patch('/schedule/deactivate/1')

    assert response.status_code == 400

@patch('shedule.schedule_table')
def test_deactivate_catches_exception(mock_db, client):
    mock_db.search.side_effect = Exception

    response = client.patch('/schedule/deactivate/1')

    assert response.status_code == 500

@patch('shedule.schedule_table')
def test_activate_returns_200_when_schedule_found(mock_db, schedule_object, client):
    mock_db.search.return_value = [schedule_object]
    mock_db.get.return_value = schedule_object

    response = client.patch('/schedule/activate/1')

    assert response.status_code == 200

@patch('shedule.schedule_table')
def test_activate_returns_400_when_schedule_not_found(mock_db, client):
    mock_db.search.return_value = []

    response = client.patch('/schedule/activate/1')

    assert response.status_code == 400

@patch('shedule.schedule_table')
def test_activate_catches_exception(mock_db, client):
    mock_db.search.side_effect = Exception

    response = client.patch('/schedule/activate/1')

    assert response.status_code == 500



