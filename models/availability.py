#!/usr/bin/python3
"""Holds the Availability class."""

import models
import sqlalchemy
from sqlalchemy import Column, Integer, Enum, Time, ForeignKey
from app import Base
from sqlalchemy.orm import relationship


class Availability(Base):
    __tablename__ = 'Availability'
    AvailabilityID = Column(Integer, primary_key=True)
    DoctorID = Column(Integer, ForeignKey('Doctors.DoctorID'),
                      nullable=True)
    DayOfWeek = Column(Enum('Monday', 'Tuesday', 'Wednesday',
                            'Thursday', 'Friday'), nullable=True)
    StartTime = Column(Time, nullable=True)
    EndTime = Column(Time, nullable=True)

    doctor = relationship("Doctor", back_populates="availabilities")

    def serialize(self):
        """Serialize Availability object to a dictionary."""
        return {
                'AvailabilityID': self.AvailabilityID,
                'DoctorID': self.DoctorID,
                'DayOfWeek': self.DayOfWeek,
                'StartTime': str(self.StartTime),
                'EndTime': str(self.EndTime)
        }
