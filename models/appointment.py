#!/usr/bin/python3
"""Defines the Appointment class."""
from models.base_model import BaseModel

class Appointment(BaseModel):
     """Represents a Appointment class.

     Attributes:
     patient_id (str): The patient idetification.
     doctor_id (str): The doctor identification.
     date (): the date of the appointment.
     time(): The time of the appointment.
     """
     patient_id = ""
     doctor_id = ""
     date = ""
     time = ""

