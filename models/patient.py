#!/usr/bin/python3
"""Defines the Patient class."""

from model.base_model import BaseModel

class Patient(BaseModel):
    """Represents a Patient.

    Attributes:

    name (str): The name of the patient
    age (int): The age of the patient
    gender (str): The gender of the patient
    username (str): username of the patient
    email (str): the email of the patient account
    password (str): the password of the patient account
    user_id (str): the user id of the patient
    """
    name = ""
    age = 0
    gender = ""
    username = ""
    email = ""
    password = ""
    user_id = ""
