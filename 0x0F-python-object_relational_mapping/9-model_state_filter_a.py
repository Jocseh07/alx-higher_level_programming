#!/usr/bin/python3
"""List all states with name from database."""
import sys

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
    Session = sessionmaker(engine)
    session = Session()
    all = session.query(State).filter(State.name.like("%a%"))
    for instance in all:
        print(instance.id, instance.name, sep=": ")
