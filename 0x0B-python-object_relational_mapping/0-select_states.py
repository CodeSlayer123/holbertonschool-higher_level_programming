#!/usr/bin/python3
"""lists all states from the database"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    mycursor = db.cursor()

    sql = "SELECT * FROM states ORDER BY id ASC"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for i in result:
        print(i)

    db.close()
