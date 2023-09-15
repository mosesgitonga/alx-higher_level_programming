#!/usr/bin/python3

import MySQLdb
from sys import argv

db = MySQLdb.connect(
    user=argv[1], passwd=argv[2], host='localhost', port=3306, db=argv[3]
    )

cur = db.cursor()

cur.execute("SELECT cities.name FROM \
    cities JOIN states ON cities.state_id = states.id\
    WHERE states.name = %s ORDER BY cities.id ASC", (argv[4], ))
cities = []
for city in cur.fetchall():
    cities.append(city[0])
print(', '.join(cities))
