#!/usr/bin/python3
"""Defines the Doctor class."""
from models.base_model import BaseModel

class Doctor(BaseModel):
    """Represents a doctor class.
    Attribeutes:

    fullname (str): The name of the doctor.
    specialty (str): The doctor's specialty.
    doctor_id (str): The doctor's id.
    """

    fullname = ""
    specialty = ""
    doctor_id = ""
