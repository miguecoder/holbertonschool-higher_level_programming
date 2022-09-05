#!/usr/bin/python3
"""
script that prints the first State object from the database hbtn_0e_6_usa
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
    Save in a temp varieble that is a
    instance
    """
    temp = session.query(State).order_by(State.id).first()

    """
    If the table states is empty, print Nothing
    followed by a new line
    """
    if temp is None:
        print("Nothing")
    else:
        print(f"{temp.id}: {temp.name}")
