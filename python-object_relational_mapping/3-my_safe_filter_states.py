#!/usr/bin/python3
"""Takes in arguments and displays all values safe from MySQL injection."""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="127.0.0.1",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    c = db.cursor()
    state_name = sys.argv[4]
    c.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
              (state_name,))
    for row in c.fetchall():
        print(row)
    c.close()
    db.close()
