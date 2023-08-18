#!/usr/bin/python3
"""
This script lists all states from a MySQL database.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cur = db.cursor()
    state_name = argv[4]
    cur.execute(
            "SELECT cities.name FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "WHERE states.name = %s "
            "ORDER BY cities.id",
            (state_name,)
            )

    rows = cur.fetchall()

    cities = ', '.join(row[0] for row in rows)
    print(cities)
    cur.close()
    db.close()
