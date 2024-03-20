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
    patients = []  # Placeholder, replace with actual logic
    return jsonify(patients)


@app.route('/patients/<int:patient_id>', methods=['GET'], strict_slashes=False)
def get_patient(patient_id):
    patient = get_patient_by_id(patient_id)
    if patient:
        return jsonify(patient.serialize())
    else:
        return jsonify({'error': 'Patient not found'}), 404


@app.route('/patients', methods=['POST'], strict_slashes=False)
def register_patient():
    data = request.get_json()
    # Implement registration logic here using data from request
    return jsonify({'message': 'Patient registered successfully'})


@app.route('/patients/<int:patient_id>', methods=['PUT'], strict_slashes=False)
def update_patient(patient_id):
    data = request.get_json()
    update_patient_details(patient_id, data)
    return jsonify({'message': 'Patient details updated successfully'})


@app.route('/patients/<int:patient_id>', methods=['DELETE'],
           strict_slashes=False)
def delete_patient(patient_id):
    # Implement delete logic here
    return jsonify({'message': 'Patient deleted successfully'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
