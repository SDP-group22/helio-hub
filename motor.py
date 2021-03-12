from tinydb import TinyDB, Query, where
from db_handler import DbHandler
from scheduler import Scheduler
from motor_controller import MotorController, UncalibratedMotorError
import utils

db = TinyDB('./database/motors.json')


def get(motor_id):
    try:
        db_handler = DbHandler.get_instance()
        motor_exists = db_handler.contains(db, id)

        if motor_exists:
            motor = db_handler.read(db, motor_id)
            return motor, 200
        else:
            return f"Motor {motor_id} not found", 404
    except:
        return 'Internal server error', 500


def get_all():
    try:
        db_handler = DbHandler.get_instance()
        all_motors = db_handler.read_all(db)
        return all_motors, 200
    except:
        return 'Internal server error', 500


def register(body):
    try:
        ip = body['ip']
        battery = body['battery']
        level = body['level']

        if not utils.valid_ip(ip):
            return f'Could not register: Invalid ip {ip}', 400

        if not (0 <= battery <= 100):
            return f'Could not register: Invalid battery level {battery}', 400

        if not (0 <= level <= 100):
            return f'Could not register: Invalid level {level}', 400

        db_handler = DbHandler.get_instance()
        all_motors = db_handler.read_all(db)
        ids = [motor['id'] for motor in all_motors]

        if ids:
            largest_id = max(ids)
            body['id'] = largest_id + 1
        else:
            body['id'] = 0

        db_handler.write(db, body)

        new_motor = db_handler.read(db, body['id'])
        return new_motor, 200
    except Exception as e:
        print(str(e))
        return 'Internal server error', 500


def unregister(motor_id):
    try:
        db_handler = DbHandler.get_instance()
        motor_exists = db_handler.contains(db, motor_id)

        if motor_exists:
            db_handler.delete(db, motor_id)
            return f"Motor {motor_id} unregistered", 200
        else:
            return f"Motor {motor_id} does not exist", 404
    except:
        return 'Internal server error', 500


def update(motor_id, body):
    try:
        ip = body['ip']
        battery = body['battery']
        level = body['level']

        if not utils.valid_ip(ip):
            return f'Could not update: Invalid ip {ip}', 400

        if not (0 <= battery <= 100):
            return f'Could not update: Invalid battery level {battery}', 400

        if not (0 <= level <= 100):
            return f'Could not update: Invalid level {level}', 400

        db_handler = DbHandler.get_instance()
        motor_exists = db_handler.contains(db, motor_id)

        if motor_exists:
            old_blind_level = db_handler.read(db, motor_id)['level']

            db_handler.update(db, motor_id, body)

            updated_motor = db_handler.read(db, motor_id)

            new_blind_level = level

            if not old_blind_level == new_blind_level:
                try:
                    MotorController.move(updated_motor, new_blind_level)
                except UncalibratedMotorError:
                    return f"Motor {motor_id} is not calibrated"

            return updated_motor, 200
        else:
            return f"Motor {motor_id} does not exist", 404
    except Exception as e:
        print(str(e))
        return 'Internal server error', 500


def calibration_start(motor_id):
    try:
        db_handler = DbHandler.get_instance()
        motor_exists = db_handler.contains(db, motor_id)

        if motor_exists:
            Scheduler.get_instance().pause()

            return "Calibration started", 200
        else:
            return f"Motor {motor_id} does not exist", 404
    except Exception as e:
        print(str(e))
        return 'Internal server error', 500


def calibration_stop(motor_id):
    try:
        db_handler = DbHandler.get_instance()
        motor_exists = db_handler.contains(db, motor_id)

        if motor_exists:
            Scheduler.get_instance().resume()

            return "Calibration finished", 200
        else:
            return f"Motor {motor_id} does not exist", 404
    except Exception as e:
        print(str(e))
        return 'Internal server error', 500


def calibration_move_up(motor_id):
    try:
        db_handler = DbHandler.get_instance()
        motor_exists = db_handler.contains(db, motor_id)

        if motor_exists:
            motor = db_handler.read(db, motor_id)
            MotorController.move_up(motor)

            return "Blinds moving up", 200
        else:
            return f"Motor {motor_id} does not exist", 404
    except Exception as e:
        print(str(e))
        return 'Internal server error', 500


def calibration_move_down(motor_id):
    try:
        db_handler = DbHandler.get_instance()
        motor_exists = db_handler.contains(db, motor_id)

        if motor_exists:
            motor = db_handler.read(db, motor_id)
            MotorController.move_down(motor)

            return "Blinds moving down", 200
        else:
            return f"Motor {motor_id} does not exist", 404
    except Exception as e:
        print(str(e))
        return 'Internal server error', 500


def calibration_stop_moving(motor_id):
    try:
        db_handler = DbHandler.get_instance()
        motor_exists = db_handler.contains(db, motor_id)

        if motor_exists:
            motor = db_handler.read(db, motor_id)
            MotorController.stop(motor)

            return "Blinds stopped", 200
        else:
            return f"Motor {motor_id} does not exist", 404
    except Exception as e:
        print(str(e))
        return 'Internal server error', 500


def calibration_set_highest(motor_id):
    try:
        db_handler = DbHandler.get_instance()
        motor_exists = db_handler.contains(db, motor_id)

        if motor_exists:
            motor = db_handler.read(db, motor_id)
            highest = MotorController.get_highest(motor)
            MotorController.set_highest(motor, highest)

            return "Highest position set", 200
        else:
            return f"Motor {motor_id} does not exist", 404
    except Exception as e:
        print(str(e))
        return 'Internal server error', 500


def calibration_set_lowest(motor_id):
    try:
        db_handler = DbHandler.get_instance()
        motor_exists = db_handler.contains(db, motor_id)

        if motor_exists:
            motor = db_handler.read(db, motor_id)
            lowest = MotorController.get_lowest(motor)
            MotorController.set_lowest(motor, lowest)

            return "Lowest position set", 200
        else:
            return f"Motor {motor_id} does not exist", 404
    except Exception as e:
        print(str(e))
        return 'Internal server error', 500


# For testing only
def test_motor_movement(motor_id, body):
    motor = body
    motor['id'] = motor_id
    MotorController.move_without_calibartion(motor, 1000)
