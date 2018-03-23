#!/usr/bin/python3
import MySQLdb
import sys
from sqlalchemy import create_engine
from model_state import State, Base
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    search = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, db_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()
    result = session.query(State).order_by(State.id)
    count = 0
    for desired in result:
        if search == desired.name:
            print(desired.id)
            break
        count += 1
    if count == result.count():
        print('Not found')
    session.close()
