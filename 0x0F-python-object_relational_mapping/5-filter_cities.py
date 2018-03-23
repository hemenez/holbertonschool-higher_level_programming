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
    cur.execute("SELECT cities.name\
    FROM cities INNER JOIN states\
    ON cities.state_id = states.id\
    WHERE states.name=%s\
    ORDER BY cities.id", (search,))
    count = 0
    my_result = cur.fetchall()
    for city_tuple in my_result:
        print(city_tuple[0], end="")
        if count != len(my_result) - 1:
            print(', ', end="")
        count += 1
    print()
    cur.close()
    db.close()
