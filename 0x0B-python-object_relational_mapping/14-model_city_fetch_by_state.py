#!/usr/bin/python3
""" prints all City objects from database"""

if __name__ == "__main__":

    from model_state import Base, State
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import create_engine
    import sys
    from sqlalchemy.orm import Session, sessionmaker
    from model_city import City

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker()
    local_session = Session(bind=engine)

    for s, c in local_session.query(State, City)\
            .filter(State.id == City.state_id).all():
        print("{}: ({}) {}".format(s.name, c.id, c.name))

    local_session.close()
