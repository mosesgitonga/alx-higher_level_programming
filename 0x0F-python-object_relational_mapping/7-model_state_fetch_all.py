#!/usr/bin/python3

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine("mysql+pymysql://{}:{}@localhost:3306/{}".format(sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True))
    Session = sessionmaker(bind=engine)
    session = Session()


    state_data = session.query(State).order_by(State.id).all()

    for state in state_data:
        print("{}: {}".format(state.id, state.name))

    session.close()
