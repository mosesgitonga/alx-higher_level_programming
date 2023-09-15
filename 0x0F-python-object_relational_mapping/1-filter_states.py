#!/usr/bin/python3
"""filter states"""
import MySQLdb

db = MySQLdb.connect(
    host='localhost', port=3306, passwd='root', db='hbtn_0e_0_usa'
    )
cur = db.cursor()

cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id")
rows = cur.fetchall()

for row in rows:
    print(f"{row}")
