#!/usr/bin/python3
"""
script that changes the name of a State object
from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
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
    Session = sessionmaker(engine)
    session = Session()

    """
    Cicle that changes the name of a State object
    where id = 2 to New Mexico
    """
    for instance in session.query(State).order_by(State.id):
        if instance.id == 2:
            instance.name = "New Mexico"

    session.commit()
    session.close()
