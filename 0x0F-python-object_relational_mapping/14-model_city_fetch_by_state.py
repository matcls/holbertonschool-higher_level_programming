#!/usr/bin/python3
"""Print all City objects from the database hbtn_0e_14_usa."""

if __name__ == "__main__":
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    from model_city import City
    from model_state import Base, State

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(City, State).\
        filter(City.state_id == State.id).order_by(City.id)
    for city, state in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
