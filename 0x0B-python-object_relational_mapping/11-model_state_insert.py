#!/usr/bin/python3
if __name__ == "__main__":

    from model_state import Base, State
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import create_engine
    from sqlalchemy import Column, Integer, String
    import sys
    from sqlalchemy import MetaData
    from sqlalchemy.orm import Session, sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker()
    local_session = Session(bind=engine)

    s1 = State()
    s1.name = "Louisiana"

    local_session.add(s1)
    local_session.commit()

    states = local_session.query(State).filter(State.name == "Louisiana")

    print(s1.id)

    local_session.close()
