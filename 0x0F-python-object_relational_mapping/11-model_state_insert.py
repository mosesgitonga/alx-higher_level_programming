#!/usr/bin/python3
"""
adding a state
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    add a nye row
    """

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                sys.argv[1], sys.argv[2], sys.argv[3]
                )
            )
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state_name = "Louisiana"

    new_state = State(name=new_state_name)
    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()
