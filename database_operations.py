#!/usr/bin/python3

from app import Session
from models.doctor import Doctor
from models.patient import Patient
from models.appointment import Appointment
from models.specialty import Specialty
from models.location import Location
from models.review import Review
from models.availability import Availability

session = Session()

# Patient Routes
def register_patient(Username, Email, Password):
    existing_patient = session.query(Patient).filter_by(Email=Email).first()
    if existing_patient:
        return "Email is already registered. Please use a different email address."
    
    # Create a new patient
    new_patient = Patient(Username=Username, Email=Email, Password=Password)
    session.add(new_patient)
    session.commit()
    return "Patient registered successfully."


def login_patient(Email, Password):
    # Check if a patient with the provided email and password exists
    patient = session.query(Patient).filter_by(Email=Email, Password=Password).first()
    if patient:
        return f"Patient {patient.Name} logged in successfully."
    else:
        return "Invalid email or password. Please try again."

def logout_patient(patient_id):
    # Implement logout logic here
    pass

def retrieve_all_patients():
    patients = session.query(Patient).all()
    return patients


def  retrieve_patient_by_id(patient_id):
    patient = session.query(Patient).get(patient_id)
    return patient


def update_patient_details(patient_id, updated_data):
    patient = session.query(Patient).get(patient_id)
    if patient:
        for key, value in updated_data.items():
            session.commit()
            return True
    else:
        return False
    

# Doctor Routes
def retrieve_all_doctors():
    doctors = session.query(Doctor).all()
    return doctors


def retrieve_doctor_by_id(doctor_id):
    doctor = session.query(Doctor).get(doctor_id)
    return doctor


def new_doctor(FullName, SpecialtyID, LocationID, AppointmentDateTime):
    doctor = Doctor(FullName="Dr. Jessica Lee", SpecialtyID=1, LocationID=2, AppointmentDateTime="2023-09-25 09:00:00")
    session.add(doctor)
    session.commit()  # Commit the session after adding a new doctor


def update_doctor_details(doctor_id, updated_data):
    doctor = session.query(Doctor).get(doctor_id)
    # Update doctor details based on updated_data
    session.commit()  # Commit the session after updating doctor details


def delete_doctor(doctor_id):
    doctor = session.query(Doctor).get(doctor_id)
    session.delete(doctor)
    session.commit()  # Commit the session after deleting a doctor


# Appointment Routes
def retrieve_all_appointments():
    appointments = session.query(Appointment).all()
    return appointments


def retrieve_appointment_by_id(appointment_id):
    appointment = session.query(Appointment).get(appointment_id)
    return appointment


def new_appointment(patient_id, doctor_id, appointment_time):
    new_appointment = Appointment(patient_id=patient_id, doctor_id=doctor_id, appointment_time=appointment_time)
    session.add(new_appointment)
    session.commit()
    return new_appointment


def update_appointment_details(appointment_id, updated_data):
    appointment = session.query(Appointment).get(appointment_id)
    session.commit()


def delete_appointment(appointment_id):
    appointment = session.query(Appointment).get(appointment_id)
    if appointment:
        session.delete(appointment)
        session.commit()
        return True
    return False


# Location Routes
def retrieve_all_locations():
    locations = session.query(Location).all()
    return locations


def retrieve_location_by_id(location_id):
    location = session.query(Location).get(location_id)
    return location


# Specialty Routes
def retrieve_all_specialties():
    specialties = session.query(Specialty).all()
    return specialties


def retrieve_specialty_by_id(specialty_id):
    specialty = session.query(Specialty).get(specialty_id)
    return specialty


# Availability Routes
def retrieve_all_availabilities():
    availabilities = session.query(Availability).all()
    return availabilities


def retrieve_availability_by_id(availability_id):
    availability = session.query(Availability).get(availability_id)
    return availability


# Review Routes
def retrieve_all_reviews():
    reviews = session.query(Review).all()
    return reviews


def retrieve_review_by_id(review_id):
    review = session.query(Review).get(review_id)
    return review
