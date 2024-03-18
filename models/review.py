#!/usr/bin/python3
"""Holds the Review class."""


import models
import sqlalchemy
from sqlalchemy import Column, Integer, Decimal, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Review(Base):
    """Represents the Reviews from patients."""

    __tablename__ = 'Reviews'
    ReviewID = Column(Integer, primary_key=True)
    DoctorID = Column(Integer, ForeignKey('Doctor.DoctorID'), nullable=True)
    PatientID = Column(Integer, ForeignKey('Patient.PatientID'), nullable=True)
    Rating = Column(Decimal(10, 0), nullable=True)
    Comment = Column(Text, nullable=True)
    DatePosted = Column(DateTime, nullable=True)

    doctor = relationship("Doctor", back_populates="reviews")
    patient = relationship("Patient", back_populates="reviews")
