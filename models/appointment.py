#!/usr/bin/python
""" holds class Appointments"""

import models
import sqlalchemy
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app import Base


class Appointment(Base):
    """Represents of Appointment."""

    __tablename__ = 'Appointments'
    AppointmentID = Column(Integer, primary_key=True)
    PatientID = Column(Integer, ForeignKey('Patients.PatientID'),
                       nullable=True)
    DoctorID = Column(Integer, ForeignKey('Doctors.DoctorID'), nullable=True)
    AppointmentTime = Column(DateTime, nullable=True)

    patient = relationship("Patient", back_populates="appointments")
    doctor = relationship("Doctor", back_populates="appointments")

    def serialize(self):
        """Serialize Appointment object to a dictionary."""
        return {
                'AppointmentID': self.AppointmentID,
                'PatientID': self.PatientID,
                'DoctorID': self.DoctorID,
                'AppointmentTime': self.AppointmentTime.
                strftime("%Y-%m-%d %H:%M:%S") if self.AppointmentTime else None
        }
