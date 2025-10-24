#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Retrieve arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create cursor and execute query
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Print results
    for row in cursor.fetchall():
        print(row)

    # Cleanup
    cursor.close()
    db.close()
