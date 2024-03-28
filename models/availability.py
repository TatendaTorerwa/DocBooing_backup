#!/usr/bin/python3
"""Holds the Availability class."""

import sqlalchemy
from sqlalchemy import Column, Integer, Enum, Time, ForeignKey
from app import Base
from sqlalchemy.orm import relationship
from models.doctor import Doctor


class Availability(Base):
    __tablename__ = 'Availability'
    AvailabilityID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    DoctorID = Column(Integer, ForeignKey('Doctor.DoctorID'),
                      nullable=False)
    DayOfWeek = Column(Enum('Monday', 'Tuesday', 'Wednesday',
                            'Thursday', 'Friday'), nullable=False)
    StartTime = Column(Time, nullable=False)
    EndTime = Column(Time, nullable=False)

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
