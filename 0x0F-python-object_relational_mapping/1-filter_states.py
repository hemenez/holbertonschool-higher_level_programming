#!/usr/bin/python3
import MySQLdb
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name REGEXP '^N' ORDER BY id")
    my_states = cur.fetchall()
    for state in my_states:
        print(state)
    cur.close()
    db.close()
