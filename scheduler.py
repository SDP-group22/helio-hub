import threading
import datetime
import utils
from tinydb import TinyDB, Query, where
from db_handler import DbHandler
from random import randrange


class Scheduler(threading.Thread):
    instance = None
    schedule_db = TinyDB('./database/schedule.json')
    motor_db = TinyDB('./database/motors.json')

    @staticmethod
    def get_instance():
        if Scheduler.instance is None:
            Scheduler.instance = Scheduler()
            Scheduler.instance.daemon = True
            Scheduler.instance.name = 'SchedulerThread'

        return Scheduler.instance

    @staticmethod
    def has_instance():
        return Scheduler.instance is not None

    @staticmethod
    def is_running():
        return Scheduler.instance.is_alive()

    def __init__(self):
        threading.Thread.__init__(self)
        self._event = threading.Event()
        self._event.set()
        self._fulfilled_schedules_ids = []

    def run(self):
        while True:
            self._event.wait()

            db_handler = DbHandler.get_instance()
            schedules = db_handler.read_all(Scheduler.schedule_db)
            schedule_to_execute = None

            for schedule in schedules:
                if not self.is_time_to_execute(schedule):
                    continue

                if schedule['id'] in self._fulfilled_schedules_ids:
                    continue

                if schedule_to_execute is None:
                    schedule_to_execute = schedule
                    continue

                if utils.is_later(schedule['time'], schedule_to_execute['time']):
                    schedule_to_execute = schedule

            if schedule_to_execute is not None:
                all_motors = db_handler.read_all(Scheduler.motor_db)

                motors = [motor for motor in all_motors if motor['id'] in schedule['motor_ids']]

                # move blinds

                for motor in motors:
                    if not motor['active']:
                        continue

                    motor['level'] = schedule['target_level']

                    db_handler.update(Scheduler.motor_db, motor['id'], motor)

                self._fulfilled_schedules_ids.append(schedule_to_execute['id'])

    def is_time_to_execute(self, schedule):
        time = datetime.datetime.now()
        day_number = datetime.datetime.today().weekday()

        day = utils.day_number_to_day_name(day_number)
        hour = time.hour
        minute = time.minute

        if day in schedule['days'] and schedule['active']:
            scheduled_hour, scheduled_minute = schedule['time'].split(':')

            scheduled_hour = int(scheduled_hour)
            scheduled_minute = int(scheduled_minute)

            return (scheduled_hour < hour) or (scheduled_hour == hour and scheduled_minute <= minute)

    def pause(self):
        self._event.clear()

    def resume(self):
        self._event.set()
