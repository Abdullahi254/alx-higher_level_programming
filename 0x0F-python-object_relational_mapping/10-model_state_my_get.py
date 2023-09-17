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
    search = av[4]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            user, passwd, db), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(
        State.name == search).order_by(State.id).first()

    if state is not None:
        print("{:d}".format(state.id))
    else:
        print("Not found")
