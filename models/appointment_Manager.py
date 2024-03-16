#!/usr/bin/python3
"""Defines the Appointment_Manager class."""
from models.base_model import BaseModel

class Appointment_Manager(BaseModel):
    """Represents a Appointment_Manager class.

    Attributes:

    hospital (str): The hospital the patient has choosen.
    appointment (str): The appointments made.
    """
    hopsital = ""
    appointment = []
