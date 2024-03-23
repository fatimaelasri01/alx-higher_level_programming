#!/usr/bin/python3
"""takes in args and displays all vals in states table of hbtn_0e_0_usa
where name matches the argument.
But this time, write one that is safe from MySQL injections!"""
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
    cursor.execute('''SELECT * FROM states WHERE states.name LIKE BINARY %s
        ORDER BY states.id ASC''', (argv[4], ))
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
