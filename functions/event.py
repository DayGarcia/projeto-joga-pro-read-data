import functions.database as database
import consts.action as action_constants
import datetime

RUNNING = 1


def get_current_event():
    sql = "SELECT id FROM projetoevent_event WHERE is_running = '%s' LIMIT 1" % (
        RUNNING)

    return database.select(sql)
