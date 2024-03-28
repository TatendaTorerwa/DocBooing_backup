#!/usr/bin/python3
"""Defines the Doctor class."""
import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app import Base
from sqlalchemy.orm import relationship


class Doctor(Base):
    """Represents the Doctor."""

    __tablename__ = 'Doctor'
    DoctorID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    FullName = Column(String(100), nullable=True)
    SpecialtyID = Column(Integer, ForeignKey('Specialty.SpecialtyID'),
                         nullable=False)
    LocationID = Column(Integer, ForeignKey('Location.LocationID'),
                        nullable=False)
    AppointmentDateTime = Column(DateTime, nullable=True)

    specialty = relationship("Specialty", back_populates="doctors")
    location = relationship("Location", back_populates="doctors")
    appointments = relationship("Appointment", back_populates="doctor")
    reviews = relationship("Review", back_populates="doctor")
    availabilities = relationship("Availability", back_populates="doctor")


    def serialize(self):
        """Serialize Doctor object to a dictionary."""
        return {
                'DoctorID': self.DoctorID,
                'FullName': self.FullName,
                'SpecialtyID': self.SpecialtyID,
                'LocationID': self.LocationID,
                'AppointmentDateTime': self.AppointmentDateTime.
                strftime("%Y-%m-%d %H:%M:%S")
                if self.AppointmentDateTime else None
        }
