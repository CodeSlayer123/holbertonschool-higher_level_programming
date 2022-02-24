#!/usr/bin/python3
import MySQLdb
import sys

db = MySQLdb.connect(host="localhost", port=3306,
                     user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

mycursor = db.cursor()
sql = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for i in myresult:
    print(i)
