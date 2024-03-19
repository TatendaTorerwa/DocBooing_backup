#!/usr/bin/python3
"""Defines the Doctor class."""

import models
import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app import Base
from sqlalchemy.orm import relationship


class Doctor(Base):
    """Represents the Doctor."""

    __tablename__ = 'Doctor'
    DoctorID = Column(Integer, primary_key=True)
    FullName = Column(String(100), nullable=True)
    SpecialtyID = Column(Integer, ForeignKey('Specialty.SpecialtyID'),
                         nullable=True)
    LocationID = Column(Integer, ForeignKey('Location.LocationID'),
                        nullable=True)
    AppointmentDateTime = Column(DateTime, nullable=True)

    specialty = relationship("Specialty", back_populates="doctors")
    location = relationship("Location", back_populates="doctors")
