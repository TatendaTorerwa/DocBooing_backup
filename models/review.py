#!/usr/bin/python3
"""Holds the Review class."""


import models
import sqlalchemy
from app import Base
from sqlalchemy import Column, Integer, Numeric, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.doctor import Doctor
from models.patient import Patient


class Review(Base):
    """Represents the Reviews from patients."""

    __tablename__ = 'Reviews'
    ReviewID = Column(Integer, primary_key=True, autoincrement=True)
    DoctorID = Column(Integer, ForeignKey('Doctor.DoctorID'), nullable=True)
    PatientID = Column(Integer, ForeignKey('Patient.PatientID'), nullable=True)
    Rating = Column(Numeric(10, 0), nullable=True)
    Comment = Column(Text, nullable=True)
    DatePosted = Column(DateTime, nullable=True)

    doctor = relationship("Doctor", back_populates="reviews")
    patient = relationship("Patient", back_populates="reviews")

    def serialize(self):
        """Serialize Review object to a dictionary."""
        return {
                'ReviewID': self.ReviewID,
                'DoctorID': self.DoctorID,
                'PatientID': self.PatientID,
                'Rating': float(self.Rating) if self.Rating is not None
                else None,
                'Comment': self.Comment,
                'DatePosted': str(self.DatePosted) if self.DatePosted else None
        }
