#!/usr/bin/python3
"""lists all cities from the database"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    mycursor = db.cursor()
    sql = "SELECT cities.id, cities.name, states.name\
        FROM cities LEFT JOIN states ON states.id = cities.state_id"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i)
    db.close()
