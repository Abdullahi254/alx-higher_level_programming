#!/usr/bin/python3
"""Link class to table in database
"""

import sys

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


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

    states = session.query(State).order_by(State.id).all()

    print("{:d}: {:s}".format(states[0].id, states[0].name))
