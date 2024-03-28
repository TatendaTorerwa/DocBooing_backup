#!/usr/bin/python3
""" holds class Appointments"""

import sqlalchemy
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.doctor import Doctor
from models.patient import Patient
from app import Base


class Appointment(Base):
    """Represents of Appointment."""

    __tablename__ = 'Appointments'
    AppointmentID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    PatientID = Column(Integer, ForeignKey('Patient.PatientID'),
                       nullable=False)
    DoctorID = Column(Integer, ForeignKey('Doctor.DoctorID'), nullable=False)
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
