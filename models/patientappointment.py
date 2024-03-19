#!/usr/bin/python3
"""Holds the PatientAppointment class."""

import models
import sqlalchemy
from sqlalchemy import Column, Integer, DateTime, Boolean, ForeignKey
from app import Base
from sqlalchemy.orm import relationship


class PatientAppointment(Base):
    """Represents the PatientAppointment class."""
    __tablename__ = 'PatientAppointment'
    PatientAppointmentID = Column(Integer, primary_key=True)
    PatientID = Column(Integer, ForeignKey('Patient.PatientID'), nullable=True)
    AppointmentID = Column(Integer, ForeignKey('Appointment.AppointmentID'),
                           nullable=True)
    ReminderDateTime = Column(DateTime, nullable=True)
    NotificationSent = Column(Boolean, nullable=True)

    patient = relationship("Patient", back_populates="appointments")
    appointment = relationship("Appointment", back_populates="patients")
