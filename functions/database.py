import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect(host="localhost",
                            database="projetojogapro",
                            user="postgres",
                            password="root")


def insert(sql, sss):
    """Inserts a new row into the database"""
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute(sql, sss)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cur.close()
        return 1
    cur.close()


def update(sql, sss):
    """Updates a row in the database"""
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute(sql, sss)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cur.close()
        return 1
    cur.close()


def select(sql):
    """Selects a row from the database"""
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql)
    recset = cur.fetchall()
    data = []
    for row in recset:
        data.append(row)
    cur.close()
    return data
