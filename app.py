#!/usr/bin/python3
"""Creating a database engine."""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

"""Database URL."""
mysql_db_url = "mysql://root:Torerwa1998!@localhost:3306/DocBooking"

"""Create database engine."""
engine = create_engine(mysql_db_url)

try:
    conn = engine.connect()
    print('db.connected')
    print('Connection object is :{}'.format(conn))
except Exception as e:
    print('db not connected:', e)

"""Create a session factory."""
Session = sessionmaker(bind=engine)

"""Base class for declarative ORM models."""
Base = declarative_base()

"""Create database tables based on the defined models."""
Base.metadata.create_all(engine)
