#!/usr/bin/python3
"""
 prints all City objects from the database
 """

from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                argv[1], argv[2], argv[3])
            )

    Session = sessionmaker(bind=engine)
    session = Session()

    for state, city in session.query(State, City).join(City):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
