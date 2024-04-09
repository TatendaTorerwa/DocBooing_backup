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

@app.route('/api/login/patient', methods=['POST'], strict_slashes=False)
def login():
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if email and password:
            result = login_patient(email, password)
            return jsonify({'message': result})
        else:
            return jsonify({'message': 'Email and password are required.'}), 400
    else:
        return jsonify({'message': 'Method not allowed.'}), 405


@app.route('/api/logout/patient', methods=['POST'], strict_slashes=False)
def logout_patient_route():
    if request.method == 'POST':
        result = logout_patient()
        return jsonify({'message': result})
    else:
        return jsonify({'message': 'Method not allowed.'}), 405

@app.route('/api/patients', methods=['GET'], strict_slashes=False)
def get_all_patients():
    """Implement logic to get all patients."""
    patients = retrieve_all_patients()
    return jsonify([patient.serialize() for patient in patients])


@app.route('/api/patients/<int:patient_id>', methods=['GET'], strict_slashes=False)
def get_patient(patient_id):
    patient = retrieve_patient_by_id(patient_id)
    if patient:
        return jsonify(patient.serialize())
    else:
        return jsonify({'error': 'Patient not found'}), 404


@app.route('/api/patients', methods=['POST'], strict_slashes=False)
def new_patient():
    data = request.get_json()
    result = register_patient(data.get('Username'), data.get('Email'), data.get('Password'))
    return jsonify({'message': result})

@app.route('/api/patients/<int:patient_id>', methods=['PUT'], strict_slashes=False)
def update_patient(patient_id):
    data = request.get_json()
    update_patient_details(patient_id, data)
    return jsonify({'message': 'Patient details updated successfully'})

@app.route('/api/patients/<int:patient_id>', methods=['DELETE'], strict_slashes=False)
def delete_patient(patient_id):
    success, message = delete_patient_from_db(patient_id)
    if success:
        return jsonify({'message': message}), 200
    else:
        return jsonify({'error': message}), 404


"""Routes for doctor operations."""


@app.route('/api/login/doctor', methods=['POST'], strict_slashes=False)
def login_doctor_route():
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if email and password:
            result = login_doctor(email, password)
            return jsonify({'message': result})
        else:
            return jsonify({'message': 'Email and password are required.'}), 400
    else:
        return jsonify({'message': 'Method not allowed.'}), 405


@app.route('/api/logout/doctor', methods=['POST'], strict_slashes=False)
def logout_doctor_route():
    if request.method == 'POST':
        result = logout_doctor()
        return jsonify({'message': result})
    else:
        return jsonify({'message': 'Method not allowed.'}), 405


@app.route('/api/doctors', methods=['GET'], strict_slashes=False)
def get_all_doctors():
	try:
		doctors = retrieve_all_doctors()
		return jsonify([doctor.serialize() for doctor in doctors])
	except Exception as e:
		print("Error fetching doctors:", e)
		return jsonify({'erroe': 'An error occurred while fetching doctors'}), 500


@app.route('/api/doctors/<int:doctor_id>', methods=['GET'], strict_slashes=False)
def get_doctor(doctor_id):
    doctor = retrieve_doctor_by_id(doctor_id)
    if doctor:
        return jsonify(doctor.serialize())
    else:
        return jsonify({'error': 'Doctor not found'}), 404


@app.route('/api/doctors', methods=['POST'], strict_slashes=False)
def add_new_doctor():
    data = request.get_json()
    new_doctor(data['FullName'], data['SpecialtyID'], data['LocationID'], data['AppointmentDateTime'], data['Email'], data['Password'])
    return(jsonify({'message': 'Doctor added successfully'}))


@app.route('/api/doctors/<int:doctor_id>', methods=['PUT'], strict_slashes=False)
def update_doctor(doctor_id):
    data = request.get_json()
    update_doctor_details(doctor_id, data)
    return jsonify({'message': 'Doctor details updated successfully'})


@app.route('/api/doctors/<int:doctor_id>',
           methods=['DELETE'], strict_slashes=False)
def delete_doctor(doctor_id):
    delete_doctor_from_db(doctor_id)
    return jsonify({'message': 'Doctor deleted successfully'})


"""Routes for appointment operations."""


@app.route('/api/appointments', methods=['GET'], strict_slashes=False)
def get_all_appointments():
    appointments = retrieve_all_appointments()
    return jsonify([appointment.serialize() for appointment in appointments])


@app.route('/api/appointmenets/<int:appointment_id>',
           methods=['GET'], strict_slashes=False)
def get_appointment(appointment_id):
    appointment = retrieve_appointment_by_id(appointment_id)
    if appointment:
        return jsonify(appointment.serialize())
    else:
        return jsonify({'error': 'Appointment not found'}), 404


@app.route('/api/appointments', methods=['POST'], strict_slashes=False)
def add_new_appointment():
    data = request.get_json()
    PatientID = data.get('PatientID')
    DoctorID = data.get('DoctorID')
    AppointmentTime = data.get('AppointmentTime')
    
    if None in (PatientID, DoctorID, AppointmentTime):
        return jsonify({'error': 'PatientID, DoctorID, and AppointmentTime are required fields'}), 400

    new_appointment_instance = new_appointment(PatientID, DoctorID, AppointmentTime)
    return jsonify({'message': 'Appointment added successfully'})


@app.route('/api/appointments/<int:appointment_id>',
           methods=['PUT'], strict_slashes=False)
def update_appointment(appointment_id):
    data = request.get_json()
    update_appointment_details(appointment_id, data)
    return jsonify({'message': 'Appointment details updated successfully'})


@app.route('/api/appointments/<int:AppointmentID>',
           methods=['DELETE'], strict_slashes=False)
def delete_appointment(AppointmentID):
    delete_appointment_route(AppointmentID)
    return jsonify({'message': 'Appointment deleted successfully'})


"""Routes for Specialties operations."""


@app.route('/api/specialties', methods=['GET'], strict_slashes=False)
def get_all_specialties():
    specialties = retrieve_all_specialties()
    return jsonify([specialty.serialize() for specialty in specialties])


@app.route('/api/specialties/<int:specialty_id>',
           methods=['GET'], strict_slashes=False)
def get_specialty(specialty_id):
    specialty = retrieve_specialty_by_id(specialty_id)
    if specialty:
        return jsonify(specialty.serialize())
    else:
        return jsonify({'error': 'specialty not found'}), 404


@app.route('/api/specialties', methods=['POST'])
def add_specialty_route():
    data = request.get_json()
    if 'SpecialtyName' in data:
        new_specialty = add_specialty_to_database(data['SpecialtyName'])
        if new_specialty:
            return jsonify({'message': 'Specialty added successfully', 'specialty': {'SpecialtyID': new_specialty.SpecialtyID, 'SpecialtyName': new_specialty.SpecialtyName}}), 201
        else:
            return jsonify({'message': 'Failed to add specialty'}), 400
    else:
        return jsonify({'message': 'SpecialtyName field is required'}), 400


@app.route('/api/specialties/<int:SpecialtyID>', methods=['PUT'])
def update_specialty_route(SpecialtyID):
    data = request.get_json()
    if 'SpecialtyName' in data:
        updated_specialty = update_specialty_in_database(SpecialtyID, data['SpecialtyName'])
        if updated_specialty:
            return jsonify({'message': 'Specialty updated successfully', 'specialty': {'SpecialtyID': updated_specialty.SpecialtyID, 'SpecialtyName': updated_specialty.SpecialtyName}}), 200
        else:
            return jsonify({'message': 'Specialty not found'}), 404
    else:
        return jsonify({'message': 'SpecialtyName field is required'}), 400


@app.route('/api/specialties/<int:SpecialtyID>', methods=['DELETE'])
def delete_specialty_route(SpecialtyID):
    if delete_specialty_from_database(SpecialtyID):
        return jsonify({'message': 'Specialty deleted successfully'}), 200
    else:
        return jsonify({'message': 'Specialty not found'}), 404


"""Routes for Locations operations."""


@app.route('/api/locations', methods=['GET'], strict_slashes=False)
def get_all_locations():
    locations = retrieve_all_locations()
    return jsonify([location.serialize() for location in locations])


@app.route('/api/locations/<int:location_id>',
           methods=['GET'], strict_slashes=False)
def get_location(location_id):
    location = retrieve_location_by_id(location_id)
    if location:
        return jsonify(location.serialize())
    else:
        return jsonify({'error': 'location not found'}), 404


@app.route('/api/locations', methods=['POST'])
def create_location():
    data = request.json
    location = add_location(data)
    return jsonify(location.serialize()), 201


@app.route('/api/locations/<int:location_id>', methods=['PUT'])
def update_existing_location(location_id):
    data = request.json
    location = update_location(location_id, data)
    if location:
        return jsonify(location.serialize()), 200
    return jsonify({'error': 'Location not found'}), 404


@app.route('/api/locations/<int:location_id>', methods=['DELETE'])
def delete_existing_location(location_id):
    location = delete_location(location_id)
    if location:
        return jsonify({'message': 'Location deleted successfully'}), 200
    return jsonify({'error': 'Location not found'}), 404


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
def add_review_route():
    data = request.json
    DoctorID = data.get('DoctorID')
    PatientID = data.get('PatientID')
    Rating = data.get('Rating')
    Comment = data.get('Comment')
    DatePosted = data.get('DatePosted')
    if DoctorID is None or PatientID is None or Rating is None or DatePosted is None:
        return jsonify({'error': 'Missing required fields'}), 400
    review = add_review(DoctorID, PatientID, Rating, Comment, DatePosted)
    if review:
        return jsonify({'success': 'Review added successfully', 'review': review.serialize()})
    else:
        return jsonify({'error': 'Failed to add review'}), 500


@app.route('/api/reviews/<int:ReviewID>',
           methods=['PUT'], strict_slashes=False)
def update_review_route(ReviewID):
    data = request.json
    DoctorID = data.get('DoctorID')
    Rating = data.get('Rating')
    Comment = data.get('Comment')
    DatePosted = data.get('DatePosted')
    if Rating is None or DatePosted is None:
        return jsonify({'error': 'Missing required fields'}), 400
    review = update_review(ReviewID, DoctorID, Rating, Comment, DatePosted)
    if review:
        return jsonify({'success': 'Review updated successfully', 'review': review.serialize()})
    else:
        return jsonify({'error': 'Review not found'}), 404


@app.route('/api/reviews/<int:ReviewID>', methods=['DELETE'], strict_slashes=False)
def delete_review_route(ReviewID):
    if delete_review(ReviewID):
        return jsonify({'success': 'Review deleted successfully'})
    else:
        return jsonify({'error': 'Review not found'}), 404


"""Routes for availability of the doctor."""


@app.route('/api/availabilities', methods=['GET'], strict_slashes=False)
def get_doctor_availability():
    availabilities = retrieve_all_availabilities()
    return jsonify([availability.serialize()
                    for availability in availabilities if availability is not None])


@app.route('/api/availabilities', methods=['POST'], strict_slashes=False)
def update_doctor_availability():
    data = request.get_json()
    new_availability = add_availability_db(data)
    return jsonify({'message': "Availability added successfully", 'AvailabilityID': new_availability.AvailabilityID}), 201


@app.route('/api/availabilities/<int:AvailabilityID>', methods=['PUT'], strict_slashes=False)
def update_availability_by_id(AvailabilityID):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided in the request body'}), 400
    
    # Check if DoctorID is provided in the data
    if 'DoctorID' not in data:
        return jsonify({'error': 'DoctorID is required in the request body'}), 400
    
    # Retrieve availability record from the database
    availability = session.query(Availability).get(AvailabilityID)
    if availability:
        # Update availability record attributes with data
        for key, value in data.items():
            setattr(availability, key, value)
        
        # Commit changes to the database session
        session.commit()
        
        return jsonify({'message': 'Availability updated successfully'}), 200
    else:
        return jsonify({'error': 'Availability not found'}), 404

@app.route('/api/availabilities/<int:AvailabilityID>', methods=['DELETE'], strict_slashes=False)
def delete_availability_by_id(AvailabilityID):
    if delete_availability_db(AvailabilityID):
        return jsonify({'message': 'Availability deleted successfully'}), 200
    return jsonify({'error': 'Availability not found'}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
