#!/usr/bin/python3
"""
Lists all cities of the state given as argument
from the database hbtn_0e_0_usa.
"""


if __name__ == "__main__":
    from sys import argv

    import MySQLdb

    if len(argv) == 5:
        connect = MySQLdb.connect(
            host="localhost",
            port=3306,
            charset="utf8",
            user=argv[1],
            passwd=argv[2],
            db=argv[3])

        cursor = connect.cursor()
        cursor.execute("""
            SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id LIKE states.id
            WHERE BINARY states.name LIKE %s
            ORDER BY cities.id""", (argv[4],))

        query_rows = print(", ".join([row[0] for row in cursor.fetchall()]))
        cursor.close()
        connect.close()
    else:
        print("Usage: mysql_username mysql_password database_name state_name")
