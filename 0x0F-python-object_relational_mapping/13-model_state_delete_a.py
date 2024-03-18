#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter 'a' from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        DATABASE_URL = "mysql://{}:{}@localhost:3306/{}".format(
            username, password, database
        )

        engine = create_engine(DATABASE_URL)

        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        # Retrieve all state objects containing 'a' in their name
        states = session.query(State).filter(State.name.like('%a%')).all()
        for state in states:
            # Delete each state object
            session.delete(state)
        session.commit()

        session.close()
