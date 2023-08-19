#!/usr/bin/python3
"""
deleting
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    """
    database connection
    """

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                sys.argv[1], sys.argv[2], sys.argv[3]
                )
            )
    Session = sessionmaker(bind=engine)
    session = Session()

    state_with_a = session.query(State).filter(State.name.like('%a%')).all()

    if state_with_a:
        for state in state_with_a:
            session.delete(state)
        session.commit()

    session.close()
