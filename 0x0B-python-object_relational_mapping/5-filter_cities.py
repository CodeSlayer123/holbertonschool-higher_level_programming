#!/usr/bin/python3
"""lists all cities of state passed as argument"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    mycursor = db.cursor()
    sql = """SELECT cities.name FROM cities INNER JOIN states ON\
        cities.state_id = states.id AND states.name = '%s'""" % sys.argv[4]
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    flag = 1
    if len(myresult) == 0:
        print()
    for i in myresult:
        print(i[0], end="")
        if flag != len(myresult):
            print(", ", end="")
        else:
            print()
        flag += 1
    db.close()
