#!/usr/bin/python3
"""
prints the first state in a table
"""

import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    printng state
    """
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True
                )
            )

    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).first()
    if first_state is not None:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")
