#!/usr/bin/python3
"""
search a state name
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    databse path connect
    """

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True
                )
            )
    Session = sessionmaker(bind=engine)
    session = Session()

    search_name = sys.argv[4]

    state = session.query(State).filter(State.name == search_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")
