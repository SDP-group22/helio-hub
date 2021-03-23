from tinydb import TinyDB
from db_handler import DbHandler
import requests


class SensorController:
    light_sensor_db = TinyDB('./database/light-sensors.json')
    motion_sensor_db = TinyDB('./database/motion-sensors.json')

    @staticmethod
    def check_motion(motion_sensor):
        url = 'http://' + motion_sensor['ip'] + ':4310' + '/get_motion'
        response = requests.get(url=url)
        return response.json()['motion']

    @staticmethod
    def check_uv(light_sensor):
        url = 'http://' + light_sensor['ip'] + ':4310' + '/get_light'
        response = requests.get(url=url)
        return response.json()['uv']
