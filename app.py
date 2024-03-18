#!/bin/usr/python3
"""Creating a database engine."""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

"""Database URL."""
db_url = 'sqlite:///DocBooking'

"""Create database engine."""
engine = create_engine(db_url)

"""Create a session factory."""
Session = sessionmaker(bind=engine)

"""Base class for declarative ORM models."""
Base = declarative_base()

"""Create database tables based on the defined models."""
Base.metadata.create_all(engine)


