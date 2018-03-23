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
    cur.execute("SELECT cities.id, cities.name, states.name\
    FROM cities INNER JOIN states\
    ON cities.state_id = states.id\
    ORDER BY cities.id")
    my_result = cur.fetchall()
    for combo in my_result:
        print(combo)
    cur.close()
    db.close()
