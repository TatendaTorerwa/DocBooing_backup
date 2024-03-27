#!/usr/bin/python3
"""Holds the PatientAppointment class."""

import sqlalchemy
from app import Base
from sqlalchemy import Column, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from models.patient import Patient
from models.appointment import Appointment


class PatientAppointment(Base):
    """Represents the PatientAppointment class."""
    __tablename__ = 'PatientAppointment'
    PatientAppointmentID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    PatientID = Column(Integer, ForeignKey('Patient.PatientID'), nullable=False)
    AppointmentID = Column(Integer, ForeignKey('Appointment.AppointmentID'),
                           nullable=False)
    ReminderDateTime = Column(DateTime, nullable=True)
    NotificationSent = Column(Boolean, nullable=True)

    patient = relationship("Patient", back_populates="appointments")
    appointment = relationship("Appointment", back_populates="patients")

    def serialize(self):
        """Serialize PatientAppointment object to a dictionary."""
        return {
                'PatientAppointmentID': self.PatientAppointmentID,
                'PatientID': self.PatientID,
                'AppointmentID': self.AppointmentID,
                'ReminderDateTime': str(self.ReminderDateTime)
                if self.ReminderDateTime else None,
                'NotificationSent': self.NotificationSent
        }
