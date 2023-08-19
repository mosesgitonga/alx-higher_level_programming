#!/usr/bin/python3
"""
updating a state
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    updating a row
    """

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                sys.argv[1], sys.argv[2], sys.argv[3]
                )
            )
    Session = sessionmaker(bind=engine)
    session = Session()

    new_name = "New Mexico"

    state_where_id = session.query(State).filter(State.id == 2).first()
    if state_where_id:
        state_where_id.name = new_name

        session.commit()
