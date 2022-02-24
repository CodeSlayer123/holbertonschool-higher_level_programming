#!/usr/bin/python3
"""lists all states from the database"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM states ORDER BY id ASC")
    for i in mycursor.fetchall():
        print(i)

    db.close()
