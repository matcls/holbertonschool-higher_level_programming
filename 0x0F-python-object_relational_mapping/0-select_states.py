#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa:"""

from sys import argv

import MySQLdb

if __name__ == "__main__":
    connect = MySQLdb.connect(
        host="localhost",
        port=3306,
        charset="utf8",
        user=argv[1],
        passwd=argv[2],
        db=argv[3])
    cur = connect.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = [print(state) for state in cur.fetchall()]
    cur.close()
    connect.close()
