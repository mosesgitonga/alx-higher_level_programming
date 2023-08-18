#!/usr/bin/python3
"""
importing modules
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    acces the database
    """

    db = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            port=3306,
            passwd=argv[2],
            db=argv[3]
            )

    cur = db.cursor()
    search = argv[4]

    cur.execute("SELECT id, name FROM states WHERE name LIKE \
            BINARY '{}' ORDER BY id".format(argv[4]))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
