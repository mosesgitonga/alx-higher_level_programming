#!/usr/bin/python3
"""filter state by user input"""

from sys import argv
import MySQLdb
if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], port=3306, db=argv[3]
        )
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE states.name='{}'".format(argv[4]))

    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    db.close()
