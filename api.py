#!/usr/bin/python3
"""Restful api."""

from flask import Flask, jsonify, request
from flask_cors import CORS
from database_operations import *

"""Creating an instance of flask."""
app = Flask(__name__)
CORS(app)

"""A route handler for the root URL."""


@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the DocBooking'})


"""Define routes for patient operations."""


@app.route('/patients', methods=['GET'], strict_slashes=False)
def get_all_patients():
    """Implement logic to get all patients."""
    patients = retrieve_all_patients()
    return jsonify([patient.serialize() for patient in patients])


@app.route('/patients/<int:patient_id>', methods=['GET'], strict_slashes=False)
def get_patient(patient_id):
    patient = retrieve_patient_by_id(patient_id)
    if patient:
        return jsonify(patient.serialize())
    else:
        return jsonify({'error': 'Patient not found'}), 404


@app.route('/patients', methods=['POST'], strict_slashes=False)
def register_patient():
    data = request.get_json()
    register_patient(data)
    return jsonify({'message': 'Patient registered successfully'})


@app.route('/patients/<int:patient_id>', methods=['PUT'], strict_slashes=False)
def update_patient(patient_id):
    data = request.get_json()
    update_patient_details(patient_id, data)
    return jsonify({'message': 'Patient details updated successfully'})


@app.route('/patients/<int:patient_id>', methods=['DELETE'],
           strict_slashes=False)
def delete_patient(patient_id):
    delete_patient(patient_id)
    return jsonify({'message': 'Patient deleted successfully'})


"""Routes for doctor operations."""


@app.route('/doctors', methods=['GET'], strict_slashes=False)
def get_all_doctors():
	try:
		doctors = retrieve_all_doctors()
		return jsonify([doctor.serialize() for doctor in doctors])
	except Exception as e:
		print("Error fetching doctors:", e)
		return jsonify({'erroe': 'An error occurred while fetching doctors'}), 500


@app.route('/doctors/<int:doctor_id>', methods=['GET'], strict_slashes=False)
def get_doctor(doctor_id):
    doctor = retrieve_doctor_by_id(doctor_id)
    if doctor:
        return jsonify(doctor.serialize())
    else:
        return jsonify({'error': 'Doctor not found'}), 404


@app.route('/doctors', methods=['POST'], strict_slashes=False)
def add_new_doctor():
    data = request.get_json()
    new_doctor(data)
    return(jsonify({'message': 'Doctor added successfully'}))


@app.route('/doctors/<int:doctor_id>', methods=['PUT'], strict_slashes=False)
def update_doctor(doctor_id):
    data = request.get_json()
    update_doctor_details(doctor_id, data)
    return jsonify({'message': 'Doctor details updated successfully'})


@app.route('/doctors/<int:doctor_id>',
           methods=['DELETE'], strict_slashes=False)
def delete_doctor(doctor_id):
    delete_doctor(doctor_id)
    return jsonify({'message': 'Doctor deleted successfully'})


"""Routes for appointment operations."""


@app.route('/appointments', methods=['GET'], strict_slashes=False)
def get_all_appointments():
    appointments = retrieve_all_appointments()
    return jsonify([appointment.serialize() for appointment in appointments])


@app.route('/appointmenets/<int:appointment_id>',
           methods=['GET'], strict_slashes=False)
def get_appointment(appointment_id):
    appointment = retrieve_appointment_by_id(appointment_id)
    if appointment:
        return jsonify(appointment.serialize())
    else:
        return jsonify({'error': 'Appointment not found'}), 404


@app.route('/appointments', methods=['POST'], strict_slashes=False)
def add_new_appointment():
    data = requests.get_json()
    add_new_appointment(data)
    return jsonify({'message': 'Appointmnet added successfully'})


@app.route('/appointments/<int:appointment_id>',
           methods=['PUT'], strict_slashes=False)
def update_appointment(appointment_id):
    data = request.get_json()
    update_appointment_details(appointment_id, data)
    return jsonify({'message': 'Appointment details updated successfully'})


@app.route('/appointments/<int:appointment_id>',
           methods=['DELETE'], strict_slashes=False)
def delete_appointment(appointment_id):
    delete_appointment(appointmet_id)
    return jsonify({'message': 'Appointment deleted successfully'})


"""Routes for Specialties operations."""


@app.route('/specialties', methods=['GET'], strict_slashes=False)
def get_all_specialties():
    specialties = retrieve_all_specialties()
    return jsonify([specialty.serialize() for specialty in specialties])


@app.route('/specialties/<int:specialty_id>',
           methods=['GET'], strict_slashes=False)
def get_specialty(specialty_id):
    specialty = retrieve_specialty_by_id(specialty_id)
    if specialty:
        return jsonify(specialty.serialize())
    else:
        return jsonify({'error': 'specialty not found'}), 404


"""Routes for Locations operations."""


@app.route('/locations', methods=['GET'], strict_slashes=False)
def get_all_locations():
    locations = retrieve_all_locations()
    return jsonify([location.serialize() for location in locations])


@app.route('/locations/<int:location_id>',
           methods=['GET'], strict_slashes=False)
def get_location(location_id):
    if location:
        return jsonify(location.serialize())
    else:
        return jsonify({'error': 'location not found'}), 404


"""Routes for Reviws from patients about Doctors."""


@app.route('/api/reviews', methods=['GET'], strict_slashes=False)
def get_all_reviews():
    reviews = retrieve_all_reviews()
    return jsonify([review.serialize() for review in reviews])


@app.route('/api/reviews/<int:review_id>',
           methods=['GET'], strict_slashes=False)
def get_review(review_id):
    review = retrieve_review_by_id(review_id)
    if review:
        return jsonify(review.serialize())
    else:
        return jsonify({'error': 'Review not found'}), 404


@app.route('/api/reviews', methods=['POST'], strict_slashes=False)
def add_review():
    data = request.get_json()
    add_new_review(data)
    return jsonify({'message': 'Review added successfully'})


@app.route('/api/reviews/<int:review_id>',
           methods=['PUT'], strict_slashes=False)
def update_review(review_id):
    data = request.get_json()
    update_review_details(review_id, data)
    return jsonify({'message': 'Review details updated successfully'})


@app.route('/api/reviews/<int:review_id>',
           methods=['DELETE'], strict_slashes=False)
def delete_review(review_id):
    delete_review(review_id)
    return jsonify({'message': 'Review deleted successfully'})


"""Routes for availability of the doctor."""


@app.route('/api/availabilities', methods=['GET'], strict_slashes=False)
def get_doctor_availability():
    availabilities = retrieve_all_availabilities()
    return jsonify([availability.serialize()
                    for availability in availabilities if availability is not None])


@app.route('/api/availabilities', methods=['POST'], strict_slashes=False)
def update_doctor_availability():
    data = request.get_json()
    update_doctor_availability(data)
    return jsonify({'message': "Doctor's availability updated successfully"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
