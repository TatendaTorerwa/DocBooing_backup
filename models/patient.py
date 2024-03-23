#!/usr/bin/python3
"""Defines the Patient class."""

import models
import sqlalchemy
from sqlalchemy import Column, Integer, String
from app import Base
from sqlalchemy.orm import relationship


class Patient(Base):
	"""Represents the Patient class."""

	__tablename__ = 'Patient'
	PatientID = Column(Integer, primary_key=True)
	Username = Column(String(50), nullable=True)
	Email = Column(String(75), nullable=True)
	Password = Column(String(30), nullable=True)
	
	appointments = relationship("Appointment", back_populates="patient")
	reviews = relationship("Review", back_populates="patient")

	def serialize(self):
		"""Serialize Patient object to a dictionary."""
		return {
			'PatientID': self.PatientID,
			'Username': self.Username,
			'Email': self.Email
		}
