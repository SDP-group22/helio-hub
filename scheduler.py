import threading
import datetime
import utils
from tinydb import TinyDB, Query, where
from db_handler import DbHandler


class Scheduler(threading.Thread):
    instance = None
    schedule_db = TinyDB('./database/schedule.json')
    motor_db = TinyDB('./database/motors.json')

    @staticmethod
    def make_instance():
        if Scheduler.instance is None:
            Scheduler.instance = Scheduler()
            Scheduler.instance.daemon = True
            Scheduler.instance.name = 'SchedulerThread'


    @staticmethod
    def get_instance():
        return Scheduler.instance

    @staticmethod
    def has_instance():
        return Scheduler.instance is not None

    @staticmethod
    def is_running():
        return Scheduler.instance.is_alive()

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            db_handler = DbHandler.get_instance()
            schedules = db_handler.read_all(Scheduler.schedule_db)

            for schedule in schedules:
                if self.is_time_to_execute(schedule):

                    all_motors = db_handler.read_all(Scheduler.motor_db)

                    motors = [motor for motor in all_motors if motor['id'] in schedule['motor_ids']]

                    # move blinds

                    for motor in motors:
                        motor['level'] = schedule['target_level']

                        db_handler.update(Scheduler.motor_db, motor['id'], motor)

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
