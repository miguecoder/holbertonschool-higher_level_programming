#!/usr/bin/python3
"""
script that prints the State object with the
name passed as argument from the database hbtn_0e_6_usa
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
    Cicle that goes through query State ordered by id
    and find the match
    """
    instance, id_found = 0, 0
    for instance in session.query(State).order_by(State.id):
        if instance.name == argv[4]:
            found_inst += 1
            id_found = instance.id
    """
    This condition is executed when a match is find
    """
    if found_inst > 0:
        print(id_found)
    else:
        print("Not found")
