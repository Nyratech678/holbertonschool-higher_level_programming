#!/usr/bin/python3
"""Takes in an argument and displays all values in the states table."""
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
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
        state_name)
    c.execute(query)
    for row in c.fetchall():
        print(row)
    c.close()
    db.close()
