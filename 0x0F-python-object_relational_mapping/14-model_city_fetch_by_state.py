#!/usr/bin/python3
import MySQLdb
import sys
from sqlalchemy import create_engine, delete
from model_state import State, Base
from model_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, db_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()
    result = session.query(State.name, City.id, City.name).filter(
        City.state_id == State.id).all()
    for city in result:
        for state in city:
            print('{}: ({}) {}'.format(state, city.id, city.name))
            break
    session.close()
