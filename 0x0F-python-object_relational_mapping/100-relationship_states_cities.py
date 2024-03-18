#!/usr/bin/python3
"""Creates the State “California” with the City “San Francisco”"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

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

        # Create California state
        california = State(name="California")
        session.add(california)
        session.flush()

        # Create San Francisco city
        san_francisco = City(name="San Francisco", state_id=california.id)
        session.add(san_francisco)

        session.commit()
