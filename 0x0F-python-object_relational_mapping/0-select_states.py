#!/usr/bin/python3.
"""
This script lists all states from a MySQL database.
"""

import MySQLdb
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        return

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connecting to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user='root',
        passwd='root',
        db='hbtn_0e_0_usa'
    )

    # Create the cursor
    cur = db.cursor()

    # Executing the query
    cur.execute("SELECT * FROM states ORDER BY id")

    # Obtain query results
    rows = cur.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cur.close()
    db.close()

if __name__ == "__main__":
    main()
