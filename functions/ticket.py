import functions.database as database
import consts.action as action_constants
import datetime


def get_ticket(event, code: str, user_id: str):
    sql = "SELECT id, status FROM projetoevent_ticket WHERE event_id = '%s' and code = '%s' and user_id = '%s' LIMIT 1" % (event,
                                                                                                                           code, user_id)

    return database.select(sql)


def log_ticket(event, code, user_id, action):
    sql = "INSERT INTO projetoevent_ticketlog (event_id, code, user_id, action, created_at, updated_at) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (
        event, code, user_id, action, datetime.datetime.now(), datetime.datetime.now())

    return database.insert(sql, None)


def update_status(event, code, user_id, status):
    sql = "UPDATE projetoevent_ticket SET status = '%s' WHERE event_id = '%s' and code = '%s' and user_id = '%s'" % (
        status + 1, event, code, user_id)

    return database.update(sql, None)


def is_valid(event, code, user_id):

    ticket = get_ticket(event, code, user_id)
    status = ticket[0][1] if len(ticket) > 0 else 0
    print('status', status)
    valid = False

    if(len(ticket) == 0):
        action = action_constants.INVALID
    elif (status == 0):
        action = action_constants.VALID
        valid = True
    else:
        action = action_constants.ALREADY_CHECKED

    log_ticket(event, code, user_id, action)
    update_status(event, code, user_id, status)

    return valid


# 0 - invalid
# 1 - valid
# 2 - already checked
