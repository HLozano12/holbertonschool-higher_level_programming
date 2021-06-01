#!/usr/bin/python3
""" List all states from database hbtn_0e_0usa """

import MySQLdb

if __name__ == "__main__":
from sys import argv

db_connection = MySQLdb.connect("localhost", 
                                argv[1],
                                argv[2],
                                argv[3])

cursor = db_connection.cursor()

cursor.execute("SELECT * FROM states")

states = cursor.fetchall()