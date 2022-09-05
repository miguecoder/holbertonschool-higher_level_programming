#!/usr/bin/python3
"""
script that prints all City objects from the database hbtn_0e_14_usa:
"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Creating connection to mysql
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1],
            argv[2],
            argv[3]
        )
    )

    """
    Setting up and starting session
    """
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    """
    Adding a new state with the State class
    """
    new_state = State(name="California")
    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)
    session.add(new_state)
    session.commit()
    session.close()
