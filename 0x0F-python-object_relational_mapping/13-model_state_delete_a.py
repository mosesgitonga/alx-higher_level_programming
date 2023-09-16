#!/usr/bin/python3
"""
delete all state with  'a'
"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv

if __name__ == '__main__':
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                argv[1], argv[2], argv[3])
            )
    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_del = session.query(State).filter(State.name.like('%a%')).all()

    for state in state_to_del:
        session.delete(state)
    session.commit()
    session.close()
