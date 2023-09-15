#!/usr/bin/python3
"""
a script that lists all State objects that\
        contain the letter a from the database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                argv[1], argv[2], argv[3], pool_pre_ping=True
                )
            )
    Session = sessionmaker(bind=engine)
    session = Session()

    state_with_a = session.query(State).filter(
            State.name.like('%a%')).order_by(State.id).all()
    for state in state_with_a:
        print("{}: {}".format(state.id, state.name))
