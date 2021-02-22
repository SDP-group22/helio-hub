from tinydb import TinyDB, Query

db = TinyDB('./database/db.json')

motor_table = db.table('motor',cache_size=0)
schedule_table = db.table('schedule',cache_size=0)