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
    Session = sessionmaker(bind=engine)
    session = Session()
    """
    cicle that print instance City and State
    to state name based on state_id, id and name
    """
    instance = session.query(City, State).join(State)
    for inst_c, inst_s in instance.all():
        print(f"{inst_s.name}: ({inst_c.id}) {inst_c.name}")

    session.commit()
    session.close()
