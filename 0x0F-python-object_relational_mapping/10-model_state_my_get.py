#!/usr/bin/python3
"""
state objects
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    hi = argv[4]
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    s = session.query(State).filter(State.name == hi).first()
    if s is None:
        print('Not found')
    else:
        print("{}".format(s.id))
    session.close()
    