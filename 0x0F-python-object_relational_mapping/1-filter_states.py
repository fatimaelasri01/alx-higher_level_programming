#!/usr/bin/python3
"""lists all states with a name starting with N (upper N)"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])

    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states WHERE name LIKE 'N%' ORDER BY
                    states.id ASC""", )
    states = cursor.fetchall()
    for state in states:
        if state[1].startswith("N"):
            print(state)
    cursor.close()
    db.close()
