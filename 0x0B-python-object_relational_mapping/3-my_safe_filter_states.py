#!/usr/bin/python3
""" SQL injection safeguard of previous task"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])

    mycursor = db.cursor()
    sql = """SELECT * FROM states WHERE name = '%s'\
        ORDER BY id ASC""" % sys.argv[4]
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i)
    db.close()
