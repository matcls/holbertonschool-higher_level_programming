#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""


if __name__ == "__main__":
    from sys import argv

    import MySQLdb

    if len(argv) == 4:
        connect = MySQLdb.connect(
            host="localhost",
            port=3306,
            charset="utf8",
            user=argv[1],
            passwd=argv[2],
            db=argv[3])

        cursor = connect.cursor()
        cursor.execute("SELECT * FROM states WHERE name LIKE BINARY \
                       'N%' ORDER BY states.id ASC")
        query_rows = [print(state) for state in cursor.fetchall()]
        cursor.close()
        connect.close()
    else:
        print("Usage: mysql_username mysql_password database_name")
