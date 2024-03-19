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
