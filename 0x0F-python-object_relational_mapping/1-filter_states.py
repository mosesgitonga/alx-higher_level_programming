#!/usr/bin/python3
"""
importing neccessary modules
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            port=3306,
            db=argv[3]
    )
    cur = db.cursor()

    cur.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
