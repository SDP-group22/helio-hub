from tinydb import TinyDB
from db_handler import DbHandler
import requests


class MotorController:
    motor_state_db = TinyDB('./database/motor_states.json')

    @staticmethod
    def move_up(motor):
        url = 'http://' + motor['ip'] + ':4310' + '/calibration_move_up'
        parameters = {'encoderValue': 100}
        r = requests.get(url=url, params=parameters)
        print(r.json())


    @staticmethod
    def move_down(motor):
        url = 'http://' + motor['ip'] + ':4310' + '/calibration_move_down'
        parameters = {'encoderValue': 100}
        r = requests.get(url=url, params=parameters)
        print(r.json())

    @staticmethod
    def stop(motor):
        url = 'http://' + motor['ip'] + ':4310' + '/calibration_stop_moving'
        requests.get(url=url)

    @staticmethod
    def get_highest(motor):
        url = 'http://' + motor['ip'] + ':4310' + '/calibration_set_highest'
        response = requests.get(url=url)
        print(response.json())
        return response.json()['highest']

    @staticmethod
    def set_highest(motor, highest):
        db_handler = DbHandler.get_instance()
        motor_has_state = db_handler.contains(MotorController.motor_state_db, motor['id'])

        if motor_has_state:
            db_handler.update(MotorController.motor_state_db, motor['id'], {'highest': highest})
        else:
            db_handler.write(MotorController.motor_state_db, {'id': motor['id'], 'highest': highest, 'lowest': None})

    @staticmethod
    def get_lowest(motor):
        url = 'http://' + motor['ip'] + ':4310' + '/calibration_set_lowest'
        response = requests.get(url=url)
        print(response.json())
        return response.json()['lowest']

    @staticmethod
    def set_lowest(motor, lowest):
        db_handler = DbHandler.get_instance()
        motor_has_state = db_handler.contains(MotorController.motor_state_db, motor['id'])

        if motor_has_state:
            db_handler.update(MotorController.motor_state_db, motor['id'], {'lowest': lowest})
        else:
            db_handler.write(MotorController.motor_state_db, {'id': motor['id'], 'highest': None, 'lowest': lowest})

    @staticmethod
    def move(motor, level):
        url = 'http://' + motor['ip'] + ':4310' + '/move'

        db_handler = DbHandler.get_instance()

        motor_has_state = db_handler.contains(MotorController.motor_state_db, motor['id'])

        if not motor_has_state:
            raise UncalibratedMotorError

        motor_state = db_handler.read(MotorController.motor_state_db, motor['id'])

        lowest = motor_state['lowest']
        highest = motor_state['highest']

        encoder_value = MotorController.level_to_encoder_value(lowest, highest, level)
        print(encoder_value)

        parameters = {'encoderValue': encoder_value}
        r = requests.get(url=url, params=parameters)

        print(r.json())

    @staticmethod
    def level_to_encoder_value(lowest, highest, new_level):
        blinds_total_range = abs(highest - lowest)
        distance_from_top = highest - ((new_level/100) * blinds_total_range)
        return distance_from_top

    # For testing only
    @staticmethod
    def move_without_calibartion(motor, encoder_value):
        url = 'http://' + motor['ip'] + ':4310' + '/move'
        parameters = {'steps': encoder_value}
        requests.get(url=url, params=parameters)


class UncalibratedMotorError(Exception):
    pass

# motor_state = {
#    'id': 0,
#    'lowest': 0,
#    'highest': 0
# }
