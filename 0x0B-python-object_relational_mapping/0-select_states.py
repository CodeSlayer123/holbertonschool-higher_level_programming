#!/usr/bin/python3
"""lists all from States table"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    myCursor = db.cursor()

    myCursor.execute("SELECT * FROM states")

    for i in myCursor.fetchall():
        print(i)

    db.close()