#!/usr/bin/python3
"""
print state object
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        ),
        pool_pre_ping=True
    )
    session = Session(engine)
    new_State = State(name="Louisiana")
    re = session.add(new_State)
    session.commit()
    print(new_State.id)
    session.close()
    