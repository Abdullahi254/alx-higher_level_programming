#!/usr/bin/python3
"""Link class to table in database
"""

import sys

from model_state import Base, State
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker, joinedload


if __name__ == "__main__":
    av = sys.argv

    user = av[1]
    passwd = av[2]
    db = av[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            user, passwd, db), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).options(
        joinedload(State.cities)).order_by(State.id).all()

    for state in states:
        for city in state.cities:
            print("{:s}: ({:d}) {:s}".format(state.name, city.id, city.name))

    session.close()
