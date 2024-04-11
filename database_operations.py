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

"""Register a new patient."""
def register_patient(Username, Email, Password):
    existing_patient = session.query(Patient).filter_by(Email=Email).first()
    if existing_patient:
        return "Email is already registered. Please use a different email address."

    
    """Create a new patient."""
    new_patient = Patient(Username=Username, Email=Email, Password=Password)
    session.add(new_patient)
    session.commit()
    return "Patient registered successfully."


"""Login a patient."""
def login_patient(Email, Password):
    """Check if a patient with the provided email and password exists."""
    patient = session.query(Patient).filter_by(Email=Email, Password=Password).first()
    if patient:
        return f"Patient {patient.Username} logged in successfully."
    else:
        return "Invalid email or password. Please try again."

"""Logout a patient."""
def logout_patient():
    return "Patient logged out successfully."


"""Retrieve all patients."""
def retrieve_all_patients():
    patients = session.query(Patient).all()
    return patients


"""Update patient details."""
def  retrieve_patient_by_id(PatientID):
    patient = session.query(Patient).get(PatientID)
    return patient


def update_patient_details(PatientID, updated_data):
    patient = session.query(Patient).get(PatientID)
    if patient:
        for key, value in updated_data.items():
           setattr(patient, key, value) 
        session.commit()
        return True
    else:
        return False

"""Delete a patient from the database."""
def delete_patient_from_db(patient_id):
    patient = session.query(Patient).get(patient_id)
    if patient:
        session.delete(patient)
        session.commit()
        return True, "Patient deleted successfully."
    else:
        return False, "Patient not found."
 

"""
Doctor Routes.
Retrieve all doctors.
"""
def retrieve_all_doctors():
    doctors = session.query(Doctor).all()
    return doctors

"""Retrieve a doctor by ID."""
def retrieve_doctor_by_id(DoctorID):
    doctor = session.query(Doctor).get(DoctorID)
    return doctor


"""Login a doctor."""
def login_doctor(Email, Password):
    """Fetch the doctor based on the provided email."""
    doctor = session.query(Doctor).filter_by(Email=Email).first()
    if doctor:
        """verify password"""
        if doctor.check_password(Password):
            return f"Doctor {doctor.FullName} logged in successfully."

    return "Invalid email or password. Please try again."


"""Logout doctor."""
def logout_doctor():
    return "Doctor logged out successfully."


"""Add a new doctor."""
def new_doctor(FullName, SpecialtyID, LocationID, AppointmentDateTime, Email, Password):
    doctor = Doctor(FullName=FullName, SpecialtyID=SpecialtyID, LocationID=LocationID, AppointmentDateTime=AppointmentDateTime, Email=Email)

    doctor.set_password(Password)

    session.add(doctor)
    session.commit()


"""Update the doctor details."""
def update_doctor_details(DoctorID, updated_data):
    doctor = session.query(Doctor).get(DoctorID)
    if doctor:
        for key, value in updated_data.items():
            setattr(doctor, key, value)
        """Update associated reviews."""
        reviews = session.query(Review).filter_by(DoctorID=DoctorID).all()

        for review in reviews:
            review.DoctorID = doctor.DoctorID
        
        session.commit()
        return True
    else:
         return False


"""Delete a doctor from the database."""
def delete_doctor_from_db(DoctorID):
    if DoctorID is None:
        """Handle the case where DoctorID is None (or any other appropriate action)."""
        return jsonify({'error': 'DoctorID cannot be None'}), 400
    
    doctor = session.query(Doctor).get(DoctorID)
    if doctor is None:
        return jsonify({'error': 'Doctor not found'}), 404
    
    session.delete(doctor)
    session.commit()
    return jsonify({'message': 'Doctor deleted successfully'}), 200


"""Appointment Routes."""

"""Retrieve all appointments."""
def retrieve_all_appointments():
    appointments = session.query(Appointment).all()
    return appointments

"""Retrieve an appointment by ID."""
def retrieve_appointment_by_id(AppointmentID):
    appointment = session.query(Appointment).get(AppointmentID)
    return appointment

"""Add a new appointment."""
def new_appointment(PatientID, DoctorID, AppointmentTime):
    new_appointment = Appointment(PatientID=PatientID, DoctorID=DoctorID, AppointmentTime=AppointmentTime)
    session.add(new_appointment)
    session.commit()
    return new_appointment

"""Update appointment details."""
def update_appointment_details(AppointmentID, updated_data):
    appointment = session.query(Appointment).get(AppointmentID)
    if appointment:
        for key, value in updated_data.items():
            setattr(appointment, key, value)
        session.commit()
        return True
    else:
        return False

"""Delete an appointment."""
def delete_appointment_route(AppointmentID):
    appointment = session.query(Appointment).get(AppointmentID)
    if appointment:
        session.delete(appointment)
        session.commit()
        return True
    return False


"""Location Routes."""

"""Retrieve all locations."""
def retrieve_all_locations():
    locations = session.query(Location).all()
    return locations

"""Retrieve a location by ID."""
def retrieve_location_by_id(LocationID):
    location = session.query(Location).get(LocationID)
    return location

"""Add a new location."""
def add_location(location_data):
    new_location = Location(**location_data)
    session.add(new_location)
    session.commit()
    return new_location

"""Update location details."""
def update_location(LocationID, location_data):
    location = session.query(Location).get(LocationID)
    if location:
        for key, value in location_data.items():
            setattr(location, key, value)
        session.commit()
    return location


"""Delete a location."""
def delete_location(LocationID):
    location = session.query(Location).get(LocationID)
    if location:
        session.delete(location)
        session.commit()
        return True
    return False


"""Specialty Routes."""

"""Retrieve all specialties."""
def retrieve_all_specialties():
    specialties = session.query(Specialty).all()
    return specialties

"""Retrieve a specialty by ID."""
def retrieve_specialty_by_id(SpecialtyID):
    specialty = session.query(Specialty).get(SpecialtyID)
    return specialty

"""Add a specialty to the database."""
def add_specialty_to_database(SpecialtyName):
    new_specialty = Specialty(SpecialtyName=SpecialtyName)
    session.add(new_specialty)
    session.commit()
    return new_specialty

"""Update a specialty in the database."""
def update_specialty_in_database(SpecialtyID, SpecialtyName):
    specialty = session.query(Specialty).get(SpecialtyID)
    if specialty:
        specialty.SpecialtyName = SpecialtyName
        session.commit()
        return specialty
    return None

"""Delete a specialty."""
def delete_specialty_from_database(SpecialtyID):
    specialty = session.query(Specialty).get(SpecialtyID)
    if specialty:
        session.delete(specialty)
        session.commit()
        return True
    return False


"""Availability Routes."""

"""Retrieve all availabilities."""
def retrieve_all_availabilities():
    availabilities = session.query(Availability).all()
    return availabilities

"""Retrieve availability by ID."""
def retrieve_availability_by_id(AvailabilityID):
    availability = session.query(Availability).get(AvailabilityID)
    return availability

"""Create a new availability."""
def add_availability_db(data):
    availability = Availability(**data)
    session.add(availability)
    session.commit()
    return availability

"""Update the availability details."""
def update_availability_db(AvailabilityID, data):
    availability = session.query(Availability).get(AvailabilityID)
    if availability:
        for key, value in data.items():
            setattr(availability, key, value)
        session.commit()
        return True
    return False

"""Delete the availability."""
def delete_availability_db(AvailabilityID):
    availability = session.query(Availability).get(AvailabilityID)
    if availability:
        session.delete(availability)
        session.commit()
        return True
    return False


"""Review Routes."""

"""Retrieve all the reviews."""
def retrieve_all_reviews():
    reviews = session.query(Review).all()
    return reviews

"""Retrieve a review by ID."""
def retrieve_review_by_id(ReviewID):
    review = session.query(Review).get(ReviewID)
    return review

"""Create a new review."""
def add_review(DoctorID, PatientID, Rating, Comment, DatePosted):
    review = Review(DoctorID=DoctorID, PatientID=PatientID, Rating=Rating, Comment=Comment, DatePosted=DatePosted)
    session.add(review)
    session.commit()
    return review

"""Update the details of a review."""
def update_review(ReviewID, DoctorID, Rating, Comment, DatePosted):
    review = session.query(Review).get(ReviewID)
    if review:
        review.DoctorID = DoctorID
        review.Rating = Rating
        review.Comment = Comment
        review.DatePosted = DatePosted
        session.commit()
        return review
    return None

"""Delete a review."""
def delete_review(ReviewID):
    review = session.query(Review).get(ReviewID)
    if review:
        session.delete(review)
        session.commit()
        return True
    return False
