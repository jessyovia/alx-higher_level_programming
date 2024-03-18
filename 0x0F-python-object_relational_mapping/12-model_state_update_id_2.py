#!/usr/bin/python3
"""Updates the name of a State object in the database hbtn_0e_6_usa"""

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

        # Retrieve the state object with id=2
        state = session.query(State).filter_by(id=2).first()
        if state:
            # Update the name of the state
            state.name = "New Mexico"
            session.commit()

        session.close()
