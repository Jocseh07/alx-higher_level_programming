#!/usr/bin/python3
"""List all states with name from database."""
import sys

import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
    )
    cur = db.cursor()
    cur.execute(
        "SELECT cities.id, cities.name,\
    states.name FROM cities INNER JOIN states ON\
    states.id=cities.state_id WHERE states.name=%s ORDER BY cities.id",
        sys.argv[4],
    )
    rows = cur.fetchall()
    for row in rows:
        print(row, sep="")
        if row != rows[-1]:
            print(", ", sep="")
        else:
            print("")
    cur.close()
    db.close()
