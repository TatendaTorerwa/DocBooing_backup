#!/usr/bin/python3
"""Defines the Hospital class."""
from models.base_model import BaseModel

class Hospital(BaseModel):
    """Represents a hospital class.

    Attributes:

    name (str): Name of the hospital
    location (str) = location of the hospital
    doctors (str) = Names of the doctors founf at that hospital.
    """

    name = ""
    location = ""
    doctors = []
