import threading
import datetime
from tinydb import TinyDB, Query, where
from db_writer import DbWriter


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
            schedules = Scheduler.schedule_db.all()

            for schedule in schedules:
                if self.is_time_to_execute(schedule):
                    motors = [Scheduler.motor_db.get(Query().id == motor_id) for motor_id in schedule['motor_ids']]

                    # move blinds

                    for motor in motors:
                        motor['level'] = schedule['target_level']

                        dbWriter = DbWriter.get_instance()
                        dbWriter.update_db(Scheduler.motor_db, motor['id'], motor)
                        dbWriter.queue.join()

    def is_time_to_execute(self, schedule):
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        time = datetime.datetime.now()
        day_number = datetime.datetime.today().weekday()

        day = days[day_number]
        hour = time.hour
        minute = time.minute

        if day in schedule['days'] and schedule['active']:
            scheduled_hour, scheduled_minute = schedule['time'].split(':')

            scheduled_hour = int(scheduled_hour)
            scheduled_minute = int(scheduled_minute)

            return (scheduled_hour < hour) or (scheduled_hour == hour and scheduled_minute <= minute)
