#!/usr/bin/python3
"""List all cities from DB"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db_connection = MySQLdb.connect("localhost",
                                    argv[1],
                                    argv[2],
                                    argv[3])

    with db_connection.cursor() as cursor:

        cursor.execute("""SELECT cities.id, cities.name, states.name FROM cities
                       JOIN states ON cities.state_id = states.id""")

        cities = cursor.fetchall()

    for h in range(len(cities)):
        print(cities[h])
