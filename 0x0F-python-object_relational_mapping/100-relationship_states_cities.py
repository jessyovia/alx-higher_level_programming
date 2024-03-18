#!/usr/bin/python3
"""Adds the State "California" with the City "San Francisco" to the database hbtn_0e_100_usa"""

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

        new_state = State(name="California")
        new_city = City(name="San Francisco", state=new_state)
        session.add(new_state)
        session.add(new_city)
        session.commit()

        session.close()
