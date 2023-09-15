#!/usr/bin/python3
"""
 a script that prints the first State object from the database hbtn_0e_6_usa
 """
from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                argv[1], argv[2], argv[3], pool_pre_ping=True)
            )
    Session = sessionmaker(bind=engine)
    session = Session()

    """check if table is empty"""
    empty_table = session.query(State).count() == 0

    if not empty_table:
        first_state = session.query(State).first()

        print("{}: {}".format(first_state.id, first_state.name))
