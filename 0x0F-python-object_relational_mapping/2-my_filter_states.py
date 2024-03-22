#!/usr/bin/python3
"""takes in an arg&displays val in states tab where name matches the arg"""
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
    query = """SELECT * FROM states WHERE states.name LIKE BINARY '{}' ORDER BY
                    states.id ASC""".format(argv[4])
    cursor.execute(query)
    states = cursor.fetchall()
    for state in state:
        print(state)
    cursor.close()
    db.close()
