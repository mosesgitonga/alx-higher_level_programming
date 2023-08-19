#!/usr/bin/python3
"""
print states with 'a'
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
if __name__ == "__main__":
    """
    create engine
    """
    engine = create_engine(
           "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True
                )
            )

    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_a = session.query(State).filter(
            State.name.like('%a%')
            ).order_by(State.id)

    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))
