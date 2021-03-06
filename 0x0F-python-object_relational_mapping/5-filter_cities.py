#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
-Takes 4 Args
-import MySQLdb
-Only execute once
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db_connection = MySQLdb.connect('localhost',
                                    argv[1],
                                    argv[2],
                                    argv[3])

    with db_connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                cities.name
            FROM
                states
            JOIN
                cities
            ON
                states.id = cities.state_id
            WHERE
                states.name = BINARY %(states)s
            """, {
                'states': argv[4]
            })

        cities = cursor.fetchall()

    for h in range(len(cities)):
        print(cities[h][0], end="")
        if h < (len(cities) - 1):
            print("", end=", ")

    print()
