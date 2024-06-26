#!/usr/bin/python3
"""Prints the city objects from database."""

import sys

from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        )
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    all = session.query(State.name, City.id, City.name).filter(
        State.id == City.state_id
    )
    for one in all:
        print("{}: ({}) {}".format(one[0], one[1], one[2]))
