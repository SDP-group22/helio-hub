import threading
import time
from tinydb import TinyDB, Query, where
from db_handler import DbHandler
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
        self._timers = {}
        self._deactivated_motors = []

    def run(self):
        while True:
            self._event.wait()
            self.__schedule_motion_sensors_actions()
            # time.sleep(2)


    def pause(self):
        self._event.clear()

    def resume(self):
        self._event.set()

    def __schedule_motion_sensors_actions(self):
        db_handler = DbHandler.get_instance()
        motion_sensors = db_handler.read_all(SensorWatcher.motion_sensor_db)

        for motion_sensor in motion_sensors:
            all_motors = db_handler.read_all(SensorWatcher.motor_db)
            motors = [motor for motor in all_motors if motor['id'] in motion_sensor['motor_ids']]
            if motion_sensor['active']:
                motion_detected = SensorController.check_motion(motion_sensor)
                print('motion detected?', motion_detected)
                if not motion_detected:
                    print('motion not detected')
                    motion_sensor_id = motion_sensor['id']

                    if motion_sensor_id not in self._timers:
                        self._timers[motion_sensor_id] = time.time()

                    motion_sensor_id = motion_sensor['id']

                    if motors[0]['level'] != 100:
                        db_handler.update(SensorWatcher.motor_db, motion_sensor['motor_ids'][0], {'active':True,'level': 100})
                        print('sensor move motor to the bottom')
                        MotorController.move(motors[0], 100)

                    # elif (time.time() - self._timers[motion_sensor_id]) >= motion_sensor['duration_sensitivity']:
                        # all_motors = db_handler.read_all(SensorWatcher.motor_db)

                        # all_schedules = db_handler.read_all(SensorWatcher.schedule_db)

                        # motors = [motor for motor in all_motors if motor['id'] in motion_sensor['motor_ids']]

                        # for schedule in all_schedules:
                        #    scheduled_motors = schedule['motor_ids']

                        #    for motor in motors:
                        #        if motor['id'] in scheduled_motors and schedule['active']:
                        #           postpone schedules
                        #           schedule['active'] = False
                        #           db_handler.write(SensorWatcher.schedule_db,schedule)
                        #           self._postponed_schedules_ids.append(schedule['id'])

                        # deactivate motors

                        # del self._timers[motion_sensor_id]

                        # for motor in motors:
                        #     if not motor['active']:
                        #         continue
                        #     try:
                        #         MotorController.move(motor, 100)
                        #     except UncalibratedMotorError:
                        #         pass

                        #     self._deactivated_motors.append({'motor_id': motor['id'], 'level': motor['level']})

                        #     motor['active'] = False
                        #     motor['level'] = 100

                        #     db_handler.update(SensorWatcher.motor_db, motor['id'], motor)
                else:
                    print('motion detected')
                    if motors[0]['level'] != 0:
                        # what happens when motion detected
                        motion_sensor_id = motion_sensor['id']
                        db_handler.update(SensorWatcher.motor_db, motion_sensor['motor_ids'][0], {'active':True,'level': 0})
                        print('sensor move motor to the top')
                        MotorController.move(motors[0], 0)

                    # if motion_sensor_id in self._timers:
                    #     del self._timers[motion_sensor_id]

                    #     # activate deactivated motors and move to previous positions
                    #     for motor in self._deactivated_motors:
                    #         db_handler.update(SensorWatcher.motor_db, motor['id'], {'active':True,'level': motor['level']})

                    #         try:
                    #             MotorController.move(motor, motor['level'])
                    #         except UncalibratedMotorError:
                    #             pass
        # wait until blinds move
        time.sleep(3)
