from tinydb import TinyDB
from db_handler import DbHandler
import requests

motor_state_db = TinyDB('./database/motor_states.json')


def move_up(motor):
    url = 'http://' + motor['ip'] + ':4310' + '/calibration_move_up'
    requests.get(url=url)


def move_down(motor):
    url = 'http://' + motor['ip'] + ':4310' + '/calibration_move_down'
    requests.get(url=url)


def stop(motor):
    url = 'http://' + motor['ip'] + ':4310' + '/calibration_stop_moving'
    requests.get(url=url)


def get_highest(motor):
    url = 'http://' + motor['ip'] + ':4310' + '/calibration_set_highest'
    requests.get(url=url)


def get_lowest(motor):
    url = 'http://' + motor['ip'] + ':4310' + '/calibration_set_lowest'
    requests.get(url=url)


def move(motor, level):
    url = 'http://' + motor['ip'] + ':4310' + '/move'

    db_handler = DbHandler.get_instance()

    motor_has_state = db_handler.contains(motor_state_db, motor['id'])

    if not motor_has_state:
        raise UncalibratedMotorError

    motor_state = db_handler.read(motor_state_db, motor['id'])

    lowest = motor_state['lowest']
    highest = motor_state['highest']

    encoder_value = level_to_encoder_value(lowest, highest, level)
    parameters = {'steps': encoder_value}
    requests.get(url=url, params=parameters)


def level_to_encoder_value(lowest, highest, new_level):
    blinds_total_range = abs(highest - lowest)
    distance_from_top = highest - (new_level * blinds_total_range)
    return distance_from_top


class UncalibratedMotorError(Exception):
    pass

# motor_state = {
#    'lowest': 0,
#    'highest': 0
# }
