#!/usr/bin/python3
"""
Create the State California with the City San Francisco
from the database hbtn_0e_100_usa.
"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, relationship
from sys import argv
from relationship_state import State, Base, City

engine = create_engine(
    'mysql+mysqldb://{}:{}@localhost:3306/{}'
    .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

session.add(City(name="San Francisco", state=State(name="California")))
session.commit()
session.close()

