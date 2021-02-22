from schedule import Scheduler
from tiny_db_wrapper import *
from json.decoder import JSONDecodeError
import time
import os

def move_blinds(schedule):
    motor_ids = schedule['motor-ids']
    level = schedule['target-level']

    for motor_id in motor_ids:
        print(f"moving blinds {motor_id} to: {level}")

class ScheduleController:

    # stores a list of jobs with schedule id as dict key
    schedule_dict = {}

    # the schedule object that runs jobs
    scheduler = Scheduler() 

    def add_schedules(self, schedules):

        for schedule in schedules:
            if schedule['id'] not in self.schedule_dict.keys() \
                and schedule['active']:
                self.add_schedule(schedule)

    def add_schedule(self, schedule):

        schedule_id = schedule['id']
        days = schedule['days']
        time = schedule['time']

        # add schedule to dict
        self.schedule_dict[schedule_id] = schedule

        # create schedule jobs
        if 'Monday' in days:
            self.scheduler.every().monday.at(time).do(move_blinds, schedule).tag(schedule_id)
        if 'Tuesday' in days:
            self.scheduler.every().tuesday.at(time).do(move_blinds, schedule).tag(schedule_id)
        if 'Wednesday' in days:
            self.scheduler.every().wednesday.at(time).do(move_blinds, schedule).tag(schedule_id)
        if 'Thursday' in days:
            self.scheduler.every().thursday.at(time).do(move_blinds, schedule).tag(schedule_id)
        if 'Friday' in days:
            self.scheduler.every().friday.at(time).do(move_blinds, schedule).tag(schedule_id)
        if 'Saturday' in days:
            self.scheduler.every().saturday.at(time).do(move_blinds, schedule).tag(schedule_id)
        if 'Sunday' in days:
            self.scheduler.every().sunday.at(time).do(move_blinds, schedule).tag(schedule_id)

    def remove_schedules(self, db_schedules):

        db_schedule_ids = [schedule['id'] for schedule in db_schedules]

        delete_set = set()

        for schedule_id, schedule in self.schedule_dict.items():
            # remove schedules that no longer exist in db
            if schedule_id not in db_schedule_ids:
                delete_set.add(schedule_id)
                break

            # remove schedules that have been updated in the db
            # (subsequently added with add_schedules)
            for db_schedule in db_schedules:
                if db_schedule['id'] == schedule['id'] and \
                  db_schedule['last_modified'] > schedule['last_modified']:
                    delete_set.add(schedule_id)
                    break

        # must delete elements outside of loop
        for schedule_id in delete_set:
            self.scheduler.clear(schedule_id)
            del self.schedule_dict[schedule_id]

    def run(self):
        while True:
            self.scheduler.run_pending()
            self.check_schedule_changes()

    def check_schedule_changes(self):
        schedules = None

        while not schedules:
            try:
                schedules = schedule_table.all()
            except JSONDecodeError:
                time.sleep(0.5)

        self.remove_schedules(schedules)
        self.add_schedules(schedules)

sc = ScheduleController()
sc.run()
