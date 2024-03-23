#!/usr/bin/python3
"""Holds the Location class."""

import models
import sqlalchemy
from sqlalchemy import Column, Integer, String
from app import Base
from sqlalchemy.orm import relationship
from models.doctor import Doctor


class Location(Base):
	"""Represents the Location."""
	__tablename__ = 'Location'
	LocationID = Column(Integer, primary_key=True)
	LocationName = Column(String(100), nullable=True)
	Address = Column(String(150), nullable=True)
	City = Column(String(120), nullable=True)
	State = Column(String(100), nullable=True)
	Zipcode = Column(String(12), nullable=True)
	
	doctors = relationship('Doctor', back_populates='location')

	def serialize(self):
		"""Serialize Location object to a dictionary."""
		return {
			'LocationID': self.LocationID,
			'LocationName': self.LocationName,
			'Address': self.Address,
			'City': self.City,
			'State': self.State,
			'Zipcode': self.Zipcode
		}
