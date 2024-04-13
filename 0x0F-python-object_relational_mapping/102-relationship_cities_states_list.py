#!/usr/bin/python3
"""Prints the city objects from database."""

import sys

from relationship_city import City
from relationship_state import Base, State
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
    all = session.query(State).order_by(State.id)
    for instance in all:
        for cities in instance.cities:
            print(cities.id, cities.name, sep=": ", end="")
            print(" -> " + instance.name)
