#!/usr/bin/python3
"""
All states via SQLAlchemy
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                argv[1], argv[2], argv[3], pool_pre_ping=True)
            )
    Session = sessionmaker(bind=engine)
    session = Session()

    all_states = session.query(State)

    for state in all_states:
        print("{}: {}".format(state.id, state.name))
