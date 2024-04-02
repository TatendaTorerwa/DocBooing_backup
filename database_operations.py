#!/usr/bin/python3

from app import Session
from flask import jsonify
from models.doctor import Doctor
from models.patient import Patient
from models.appointment import Appointment
from models.specialty import Specialty
from models.location import Location
from models.review import Review
from models.availability import Availability
from sqlalchemy.exc import SQLAlchemyError


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
        return f"Patient {patient.Username} logged in successfully."
    else:
        return "Invalid email or password. Please try again."


def logout_patient(PatientID):
    # Implement logout logic here
    pass

def retrieve_all_patients():
    patients = session.query(Patient).all()
    return patients


def  retrieve_patient_by_id(PatientID):
    patient = session.query(Patient).get(PatientID)
    return patient


def update_patient_details(PatientID, updated_data):
    patient = session.query(Patient).get(PatientID)
    if patient:
        for key, value in updated_data.items():
            session.commit()
            return True
    else:
        return False


def delete_patient_from_db(patient_id):
    patient = session.query(Patient).get(patient_id)
    if patient:
        session.delete(patient)
        session.commit()
        return True, "Patient deleted successfully."
    else:
        return False, "Patient not found."
 

# Doctor Routes
def retrieve_all_doctors():
    doctors = session.query(Doctor).all()
    return doctors


def retrieve_doctor_by_id(DoctorID):
    doctor = session.query(Doctor).get(DoctorID)
    return doctor

def login_doctor(Email, Password):
    # Check if a doctor with the provided email and password exists
    doctor = session.query(Doctor).filter_by(Email=Email, Password=Password).first()
    if doctor:
        return f"Doctor {doctor.FullName} logged in successfully."
    else:
        return "Invalid email or password. Please try again."


def new_doctor(FullName, SpecialtyID, LocationID, AppointmentDateTime):
    doctor = Doctor(FullName=FullName, SpecialtyID=SpecialtyID, LocationID=LocationID, AppointmentDateTime=AppointmentDateTime)
    session.add(doctor)
    session.commit()  # Commit the session after adding a new doctor


def update_doctor_details(DoctorID, updated_data):
    doctor = session.query(Doctor).get(DoctorID)
    # Update doctor details based on updated_data
    session.commit()  # Commit the session after updating doctor details


def delete_doctor_from_db(DoctorID):
    if DoctorID is None:
        # Handle the case where DoctorID is None (or any other appropriate action)
        return jsonify({'error': 'DoctorID cannot be None'}), 400
    
    doctor = session.query(Doctor).get(DoctorID)
    if doctor is None:
        return jsonify({'error': 'Doctor not found'}), 404
    
    session.delete(doctor)
    session.commit()  # Commit the session after deleting a doctor
    return jsonify({'message': 'Doctor deleted successfully'}), 200


# Appointment Routes
def retrieve_all_appointments():
    appointments = session.query(Appointment).all()
    return appointments


def retrieve_appointment_by_id(AppointmentID):
    appointment = session.query(Appointment).get(AppointmentID)
    return appointment


def new_appointment(PatientID, DoctorID, AppointmentTime):
    new_appointment = Appointment(PatientID=PatientID, DoctorID=DoctorID, AppointmentTime=AppointmentTime)
    session.add(new_appointment)
    session.commit()
    return new_appointment


def update_appointment_details(AppointmentID, updated_data):
    appointment = session.query(Appointment).get(AppointmentID)
    session.commit()


def delete_appointment_route(AppointmentID):
    appointment = session.query(Appointment).get(AppointmentID)
    if appointment:
        session.delete(appointment)
        session.commit()
        return True
    return False


# Location Routes
def retrieve_all_locations():
    locations = session.query(Location).all()
    return locations


def retrieve_location_by_id(LocationID):
    location = session.query(Location).get(LocationID)
    return location


def add_location(location_data):
    new_location = Location(**location_data)
    session.add(new_location)
    session.commit()
    return new_location


def update_location(LocationID, location_data):
    location = session.query(Location).get(LocationID)
    if location:
        for key, value in location_data.items():
            setattr(location, key, value)
        session.commit()
    return location


def delete_location(LocationID):
    location = session.query(Location).get(LocationID)
    if location:
        session.delete(location)
        session.commit()
        return True
    return False


# Specialty Routes
def retrieve_all_specialties():
    specialties = session.query(Specialty).all()
    return specialties


def retrieve_specialty_by_id(SpecialtyID):
    specialty = session.query(Specialty).get(SpecialtyID)
    return specialty


def add_specialty_to_database(SpecialtyName):
    new_specialty = Specialty(SpecialtyName=SpecialtyName)
    session.add(new_specialty)
    session.commit()
    return new_specialty


def update_specialty_in_database(SpecialtyID, SpecialtyName):
    specialty = session.query(Specialty).get(SpecialtyID)
    if specialty:
        specialty.SpecialtyName = SpecialtyName
        session.commit()
        return specialty
    return None


def delete_specialty_from_database(SpecialtyID):
    specialty = session.query(Specialty).get(SpecialtyID)
    if specialty:
        session.delete(specialty)
        session.commit()
        return True
    return False


# Availability Routes
def retrieve_all_availabilities():
    availabilities = session.query(Availability).all()
    return availabilities


def retrieve_availability_by_id(AvailabilityID):
    availability = session.query(Availability).get(AvailabilityID)
    return availability


def add_availability_db(data):
    availability = Availability(**data)
    session.add(availability)
    session.commit()
    return availability


def update_availability_db(AvailabilityID, data):
    availability = session.query(Availability).get(AvailabilityID)
    if availability:
        for key, value in data.items():
            setattr(availability, key, value)
        session.commit()
        return True
    return False


def delete_availability_db(AvailabilityID):
    availability = session.query(Availability).get(AvailabilityID)
    if availability:
        session.delete(availability)
        session.commit()
        return True
    return False


# Review Routes
def retrieve_all_reviews():
    reviews = session.query(Review).all()
    return reviews


def retrieve_review_by_id(ReviewID):
    review = session.query(Review).get(ReviewID)
    return review


def add_review(DoctorID, PatientID, Rating, Comment, DatePosted):
    review = Review(DoctorID=DoctorID, PatientID=PatientID, Rating=Rating, Comment=Comment, DatePosted=DatePosted)
    session.add(review)
    session.commit()
    return review


def update_review(ReviewID, Rating, Comment, DatePosted):
    review = session.query(Review).get(ReviewID)
    if review:
        review.Rating = Rating
        review.Comment = Comment
        review.DatePosted = DatePosted
        session.commit()
        return review
    return None


def delete_review(ReviewID):
    review = session.query(Review).get(ReviewID)
    if review:
        session.delete(review)
        session.commit()
        return True
    return False
