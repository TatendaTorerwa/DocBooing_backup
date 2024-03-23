#!/bin/usr/python3
"""Holds the Specialty class."""

import models
import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from app import Base


class Specialty(Base):
    """Representstion og Specialty."""
    __tablename__ = 'Specialty'
    SpecialtyID = Column(Integer, primary_key=True)
    SpecialtyName = Column(String(80), nullable=True)

    doctors = relationship("Doctor", back_populates="specialty")


    def serialize(self):
        """Serialize Specialty object to a dictionary."""
        return {
                'SpecialtyID': self.SpecialtyID,
                'SpecialtyName': self.SpecialtyName
        }
