#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
-Takes 4 Args
-import MySQLdb
-Only execute once
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db_connection = MySQLdb.connect("localhost",
                                    argv[1],
                                    argv[2],
                                    argv[3])

    with db_connection.cursor() as cursor:
        cursor.execute({ 'states': argv[4]
        })
    citites = cursor.fetchall()

for h in range(len(cities)):
    print (citites[h][0], end="")
    if h < (len(citites) - 1):
        print("", end=", ")

print()