#!/usr/bin/python3
"""
print all cities
"""

from model_city import City, Base
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    """
    creates engine
    """
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True
                )
            )
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(State, City).filter(
            City.state_id == State.id).order_by(City.id).all()
    for state, city in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
