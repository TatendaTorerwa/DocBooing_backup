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
	PatientID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
	Username = Column(String(50), nullable=False)
	Email = Column(String(75), nullable=False)
	Password = Column(String(128), nullable=False)
	
	appointments = relationship("Appointment", back_populates="patient")
	reviews = relationship("Review", back_populates="patient")

	  def set_password(self, password):
        	"""Hashes and sets the patient's password."""
        	self.Password = bcrypt.hash(password)

	def check_password(self, password):
        	"""Verifies the provided password against the hashed password."""
        	return bcrypt.verify(password, self.Password)

	def serialize(self):
		"""Serialize Patient object to a dictionary."""
		return {
			'PatientID': self.PatientID,
			'Username': self.Username,
			'Email': self.Email
		}
