#!/usr/bin/python3
"""Holds the Specialty class."""

import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from app import Base


class Specialty(Base):
    """Representation og Specialty."""
    __tablename__ = 'Specialty'
    SpecialtyID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    SpecialtyName = Column(String(80), nullable=True)

    doctors = relationship("Doctor", back_populates="specialty")


    def serialize(self):
        """Serialize Specialty object to a dictionary."""
        return {
                'SpecialtyID': self.SpecialtyID,
                'SpecialtyName': self.SpecialtyName
        }
