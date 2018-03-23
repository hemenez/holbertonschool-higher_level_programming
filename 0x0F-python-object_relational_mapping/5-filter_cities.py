#!/usr/bin/python3
import MySQLdb
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    search = sys.argv[4]
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)
    cur = db.cursor()
    cur.execute("SELECT cities.name, states.name\
    FROM cities INNER JOIN states\
    ON cities.state_id = states.id\
    WHERE states.name=%s\
    ORDER BY cities.id", (search,))
    my_result = cur.fetchall()
    count = 0
    for combo in my_result:
        if combo[1] == search:
            if count != len(my_result) - 1:
                print(combo[0] + ', ', end="")
            else:
                print(combo[0])
            count += 1
    cur.close()
    db.close()
