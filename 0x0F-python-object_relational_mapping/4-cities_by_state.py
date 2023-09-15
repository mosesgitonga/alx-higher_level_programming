#!/usr/bin/python3

import MySQLdb
from sys import argv

db = MySQLdb.connect(user=argv[1], host='localhost', port=3306, passwd=argv[2], db=argv[3])

cur = db.cursor()

cur.execute("SELECT * FROM cities ORDER BY cities.id")

rows = cur.fetchall()
for index, row in enumerate(rows):
   print(index, row)
