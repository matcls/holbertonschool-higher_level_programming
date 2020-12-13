#!/usr/bin/python3
"""Cchanges the name of a State object from the database hbtn_0e_6_usa."""

if __name__ == "__main__":
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    from model_state import Base
    from model_state import State

    if len(argv) == 4:
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        state = session.query(State).filter(State.id == 2)
        if state:
            state[0].name = "New Mexico"
        session.commit()
        session.close()
    else:
        print("Usage: mysql_username mysql_password database_name")
