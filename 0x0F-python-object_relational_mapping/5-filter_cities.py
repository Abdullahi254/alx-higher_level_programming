#!/usr/bin/python3
"""
0-select_states - displays all the cities in a given state
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    av = sys.argv
    ac = len(av) - 1

    user = av[1]
    passwd = av[2]
    db = av[3]
    name = av[4]

    host = "localhost"
    port = 3306

    conn = MySQLdb.connect(host=host, port=port,
                           user=user, passwd=passwd, db=db)

    cur = conn.cursor()
    cur.execute(
                """SELECT c.name
                FROM cities c
                JOIN states s ON c.state_id = s.id
                WHERE s.name = _utf8mb4 %s COLLATE utf8mb4_0900_as_cs
                ORDER BY c.id ASC;""", (name,))

    rows = cur.fetchall()

    for row in rows:
        print(row[0], end=", " if row != rows[-1] else "")
    print()
