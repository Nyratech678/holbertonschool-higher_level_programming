#!/usr/bin/python3
"""Takes in the name of a state and lists all cities of that state."""
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
    c.execute("""SELECT cities.name FROM cities
                 JOIN states ON cities.state_id = states.id
                 WHERE states.name = %s
                 ORDER BY cities.id ASC""", (state_name,))
    cities = c.fetchall()
    print(", ".join([city[0] for city in cities]))
    c.close()
    db.close()
