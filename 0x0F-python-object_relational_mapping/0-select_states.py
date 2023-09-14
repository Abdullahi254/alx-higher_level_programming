#!/usr/bin/python3
"""
0-select_states - displays all values in the states table of hbtn_0e_0_usa
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    av = sys.argv
    ac = len(av) - 1

    user = av[1]
    passwd = av[2]
    db = av[3]

    host = "localhost"
    port = 3306

    conn = MySQLdb.connect(host=host, port=port,
                           user=user, passwd=passwd, db=db)

    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)
