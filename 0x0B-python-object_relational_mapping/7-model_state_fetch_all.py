#!/usr/bin/python3

if __name__ == "__main__":

    from model_state import Base, State
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import create_engine
    from sqlalchemy import Column, Integer, String
    import sys
    from sqlalchemy import MetaData
    from sqlalchemy.orm import Session, sessionmaker


    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)


    Session = sessionmaker()
    local_session = Session(bind=engine)
    states=local_session.query(State).all()

    for i in states:
        print("{}: {}".format(i.id, i.name))

    local_session.close()
