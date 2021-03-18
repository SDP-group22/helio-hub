import threading
import datetime
import utils
import time
from tinydb import TinyDB, Query, where
from db_handler import DbHandler
from random import randrange
from motor_controller import MotorController, UncalibratedMotorError
from sensor_controller import SensorController


class SensorWatcher(threading.Thread):
    instance = None
    light_sensor_db = TinyDB('./database/light-sensors.json')
    motion_sensor_db = TinyDB('./database/motion-sensors.json')
    motor_db = TinyDB('./database/motors.json')
    schedule_db = TinyDB('./database/schedule.json')

    @staticmethod
    def get_instance():
        if SensorWatcher.instance is None:
            SensorWatcher.instance = SensorWatcher()
            SensorWatcher.instance.daemon = True
            SensorWatcher.instance.name = 'SensorWatcherThread'

        return SensorWatcher.instance

    @staticmethod
    def has_instance():
        return SensorWatcher.instance is not None

    @staticmethod
    def is_running():
        return SensorWatcher.instance.is_alive()

    def __init__(self):
        threading.Thread.__init__(self)
        self._event = threading.Event()
        self._event.set()
        self._postponed_schedules_ids = []

    def run(self):
        while True:
            self._event.wait()

            time.sleep(5)

    def pause(self):
        self._event.clear()

    def resume(self):
        self._event.set()

    def __schedule_motion_sensors_actions(self):
        db_handler = DbHandler.get_instance()
        motion_sensors = db_handler.read_all(SensorWatcher.motion_sensor_db)
        timers = {}

        for motion_sensor in motion_sensors:
            if motion_sensor['active']:
                motion_detected = SensorController.check_motion(motion_sensor)

                if not motion_detected:
                    motion_sensor_id = motion_sensor['id']

                    if motion_sensor_id not in timers:
                        timers[motion_sensor_id] = time.time()

                    elif (time.time() - timers[motion_sensor_id]) >= motion_sensor['duration_sensitivity']:
                        all_motors = db_handler.read_all(SensorWatcher.motor_db)
                        all_schedules = db_handler.read_all(SensorWatcher.schedule_db)

                        motors = [motor for motor in all_motors if motor['id'] in motion_sensor['motor_ids']]

                        for schedule in all_schedules:
                            scheduled_motors = schedule['motor_ids']

                            for motor in motors:
                                if motor['id'] in scheduled_motors and schedule['active']:
                                    pass
                                    #postpone schedules

                        del timers[motion_sensor_id]

                        for motor in motors:
                            if not motor['active']:
                                continue
                            try:
                                MotorController.move(motor, 100)
                            except UncalibratedMotorError:
                                pass

                            motor['level'] = 100

                            db_handler.update(Scheduler.motor_db, motor['id'], motor)

                        # wait until blinds move
                        time.sleep(5)
                else:
                    pass
                    #what happens when motion detected