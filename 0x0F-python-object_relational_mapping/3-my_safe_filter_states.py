#!/usr/bin/python3
"""List all states from database hbtn_0e_0usa"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db_connection = MySQLdb.connect("localhost",
                                    argv[1],
                                    argv[2],
                                    argv[3])

    cursor = db_connection.cursor()

    cursor.execute("""SELECT * FROM states WHERE name = BINARY %(name)s
                   """, {'name': argv[4]})

    states = cursor.fetchall()

    for h in range(len(states)):
        print(states[h])
