#!/usr/bin/python3
"""
prevetingSQL injection
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost', user=argv[1], passwd=argv[2], db=argv[3]
        )
    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states WHERE \
states.name = %s ORDER BY states.id", (argv[4],))

    rows = cur.fetchall()
    for row in rows:
        print(row)
