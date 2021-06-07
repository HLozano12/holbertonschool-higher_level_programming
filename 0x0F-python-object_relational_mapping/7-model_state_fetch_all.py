#!/usr/bin/python3
"""LIst states from Data Base"""

from sys import argv
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Query


if __name__ == "__main__":
    the_engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}').format(
        sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True)

    Base.metadata.create_all(the_engine)

    Session = sessionmaker(bind=the_engine)

    ints_sessh = Session()

    for str in state:
        print("{}: {}".format(str.id, str.name))
