#!/usr/bin/python3
"""
lists all states in the db
"""

import MySQLdb

db = MySQLdb.connect(
    host='localhost', port=3306, passwd='root', db='hbtn_0e_0_usa'
)
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY states.id")
rows = cur.fetchall()

for row in rows:
    print(f"{row}")
