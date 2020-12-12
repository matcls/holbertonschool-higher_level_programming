#!/usr/bin/python3
"""Takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
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
        cursor.execute("SELECT * FROM states WHERE name LIKE BINARY \
                       '{}' ORDER BY states.id ASC".format(argv[4]))
        query_rows = [print(state) for state in cursor.fetchall()]
        cursor.close()
        connect.close()
    else:
        print("Usage: mysql_username mysql_password database_name")
