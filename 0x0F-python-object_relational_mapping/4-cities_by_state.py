#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_0_usa."""


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
        cursor.execute("SELECT cities.id, cities.name, states.name \
                       FROM states JOIN cities on cities.state_id = states.id \
                       ORDER BY cities.id ASC")
        query_rows = [print(state) for state in cursor.fetchall()]
        cursor.close()
        connect.close()
    else:
        print("Usage: mysql_username mysql_password database_name")
