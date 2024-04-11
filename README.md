# Project Name:  DocBooking (Backend)

## Introduction

DocBooking is an online platform designed to streamline the process of booking appointments with doctors. Our project aims to bridge the gap between patients and healthcareproviders by providing a user-friendly interface for scheduling medical consultations.

![Screenshot](blog3.png)


## Links

- Deployed Site: https://www.pythonanywhere.com/user/TatendaTorerwa/webapps/#tab_id_tatendatorerwa_pythonanywhere_com
- Final Project Blog Article:
- Author's LinkedIn:



## Installation
To set up the backend of DocBooking, follow these steps:


1. **Clone the repository:** 
git clone https://github.com/yourusername/DocBooking_backup.git

2. **Navigate to the project directory:** 
cd DocBooking_backup

3. **Install dependencies:** 
pip install -r requirements.txt

4. **Database setup:** 
- Create a MySQL database named `DocBooking`.
- Configure the database connection in the `app.py` file using SQLAlchemy.

5. **Run the Flask server:** 
python3 -m api

6. **Access the backend locally:** 
- Using curl:
  ```
  curl -X GET http://127.0.0.1:5000
  ```
- Using a web browser:
  ```
  Go to http://localhost:5000/
  ```

7. **Deployment:** 
- Deploy the backend using PythonAnywhere.
- Base endpoint: `https://tatendatorerwa.pythonanywhere.com/`.

8. **Testing endpoints:** 
- Use Postman to test the API endpoints.

Once you've completed these steps, the backend of DocBooking should be installed, configured, and ready to use both locally and in production.



## Usage

### Interacting with the API

**Base URL:** [https://tatendatorerwa.pythonanywhere.com/](https://tatendatorerwa.pythonanywhere.com/)

#### Patients

##### Get All Patients:

curl https://tatendatorerwa.pythonanywhere.com/api/patients

##### Get Patient by ID:

curl https://tatendatorerwa.pythonanywhere.com/api/patients/2

##### Create New Patient:

curl -X POST https://tatendatorerwa.pythonanywhere.com/api/patients -d '{"Username": "John", "Email": "john128@gmail.com", "Password": "john123"}' -H "Content-Type: application/json"


##### Update Patient:

curl -X PUT https://tatendatorerwa.pythonanywhere.com/api/patients/8 -d '{"Email": "john128.com"}' -H "Content-Type: application/json"

##### Delete Patient:

curl -X DELETE https://tatendatorerwa.pythonanywhere.com/api/patients/10

#### Doctors

##### Get All Doctors:

curl https://tatendatorerwa.pythonanywhere.com/api/doctors

##### Get Doctor by ID:

curl https://tatendatorerwa.pythonanywhere.com/api/doctors/2


##### Create New Doctor:

curl https://tatendatorerwa.pythonanywhere.com/api/doctors -d '{"FullName":"Dr Nobert Mureriwa", "SpecialtyID":8, "LocationID":9, "Email":"mandizvidza@gmail.com", "Password":"chidomandi@gmail.com", "AppointmentDateTime":"2024-03-27 16:00:00"}' -H "Content-Type: application/json"

##### Update Doctor:

curl https://tatendatorerwa.pythonanywhere.com/api/doctors/11 -d '{"LocationID":3, "SpecialtyID":1, "AppointmentDateTime":"2024-02-29 15:00:00"}' -H "Content-Type: application/json"

##### Delete Doctor:

curl https://tatendatorerwa.pythonanywhere.com/api/doctors/11

#### Specialty

##### Get All Specialties:

curl https://tatendatorerwa.pythonanywhere.com/api/specialties

##### Get Specialty by ID:

curl https://tatendatorerwa.pythonanywhere.com/api/specialties/8

##### Create New Specialty:

curl https://tatendatorerwa.pythonanywhere.com/api/specialties -d '{"SpecialtyName":"Beauty"}' -H "Content-Type: application/json"

##### Update Specialty:

curl https://tatendatorerwa.pythonanywhere.com/api/specialties/9 -d '{"SpecialtyName":"Dermatology"}' -H "Content-Type: application/json"

##### Delete Specialty:

curl https://tatendatorerwa.pythonanywhere.com/api/specialties/9

#### Locations

##### Get All Locations:

curl https://tatendatorerwa.pythonanywhere.com/api/locations

##### Get Location by ID:

curl https://tatendatorerwa.pythonanywhere.com/api/locations/1

##### Create New Location:

curl https://tatendatorerwa.pythonanywhere.com/api/locations -d '{"LocationName":"CraigHall", "Address":"120 Main CraigHall", "City":"Capetown", "State":"Gauteng", "Zipcode":"1000"}' -H "Content-Type: application/json"

##### Update Location:

curl https://tatendatorerwa.pythonanywhere.com/api/locations/10 -d '{"Address":"27B, Allen Avenue, CraigHall"}' -H "Content-Type: application/json"

##### Delete Location:

curl https://tatendatorerwa.pythonanywhere.com/api/locations/10

#### Appointments

##### Get All Appointments:

curl https://tatendatorerwa.pythonanywhere.com/api/appointments

##### Get Appointment by ID:

curl https://tatendatorerwa.pythonanywhere.com/api/appointments/2

##### Create New Appointment:

curl https://tatendatorerwa.pythonanywhere.com/api/appointments -d '{"PatientID":10, "DoctorID":10, "AppointmentTime":"2024-01-27 16:00:00"}' -H "Content-Type: application/json"

##### Update Appointment:

curl https://tatendatorerwa.pythonanywhere.com/api/appointments/8 -d '{"PatientID":10, "DoctorID":10, "AppointmentTime":"2023-01-27 16:00:00"}' -H "Content-Type: application/json"

##### Delete Appointment:

curl https://tatendatorerwa.pythonanywhere.com/api/appointments/8

#### Reviews

##### Get All Reviews:

curl https://tatendatorerwa.pythonanywhere.com/api/reviews

##### Get Review by ID:

curl https://tatendatorerwa.pythonanywhere.com/api/reviews/3

##### Create New Review:

curl https://tatendatorerwa.pythonanywhere.com/api/reviews -d '{ "DoctorID":10, "PatientID":10, "Rating":10, "Comment":"The Doctor is very friendly", "DatePosted":"2024-06-28T15:30:00"}' -H "Content-Type: application/json"

###### Update Review:

curl https://tatendatorerwa.pythonanywhere.com/api/reviews/10 -d '{ "DoctorID":10, "PatientID":10, "Rating":7, "Comment":"The Doctor is very friendly", "DatePosted":"2024-06-28T15:30:00"}' -H "Content-Type: application/json"

##### Delete Review:

curl https://tatendatorerwa.pythonanywhere.com/api/reviews/10

#### Availabilities

##### Get All Availabilities:

curl https://tatendatorerwa.pythonanywhere.com/api/availabilities

##### Get Availability by ID:

curl https://tatendatorerwa.pythonanywhere.com/api/availabilities/4

##### Create New Availability:

curl https://tatendatorerwa.pythonanywhere.com/api/availabilities -d '{"DoctorID":10, "DayOfWeek":"Saturday", "StartTime":"08:00:00", "EndTime":"08:45:00"}' -H "Content-Type: application/json"

##### Update Availability:

curl https://tatendatorerwa.pythonanywhere.com/api/availabilities/8 -d '{"DayOfWeek":"Wednesday", "DoctorID":10}' -H "Content-Type: application/json"

##### Delete Availability:

curl https://tatendatorerwa.pythonanywhere.com/api/availabilities/8

#### User Authentication

##### Patient Login:

curl -X POST https://tatendatorerwa.pythonanywhere.com/api/login/patient -d '{"email": "patient@example.com", "password": "password123"}' -H "Content-Type: application/json"

##### Doctor Login:

curl -X POST https://tatendatorerwa.pythonanywhere.com/api/login/doctor -d '{"email": "doctor@example.com", "password": "password123"}' -H "Content-Type: application/json"

##### Patient Logout:

curl -X POST https://tatendatorerwa.pythonanywhere.com/api/logout/patient

##### Doctor Logout:

curl -X POST https://tatendatorerwa.pythonanywhere.com/api/logout/doctor



## Contributing

We welcome contributions from the community to improve the DocBooking backend. If you'd like to contribute, please follow these guidelines:

### Bug Reports and Feature Requests

If you encounter any bugs or have ideas for new features, please open an issue on the GitHub repository. When submitting a bug report, please include detailed information about the issue, including steps to reproduce it if possible.

### Pull Requests

We encourage you to submit pull requests for bug fixes, improvements, or new features. Before submitting a pull request, please ensure the following:

- Fork the repository and create a new branch for your changes.
- Make sure your code adheres to the project's coding style and conventions.
- Write clear and descriptive commit messages.
- Test your changes thoroughly to ensure they work as expected.
- Update the documentation if necessary.

Once your changes are ready, submit a pull request to the `master` branch of the main repository. A project maintainer will review your contribution and provide feedback. Please be patient and responsive to any comments or requests for changes during the review process.

Thank you for considering contributing to the DocBooking project!



## Related projects

While there are no directly related projects to DocBooking, the project's architecture and database structure draw inspiration from the ALX Airbnb project. The modeling approach and database connections implemented in DocBooking share similarities with the ALX Airbnb project, providing a familiar structure for users familiar with that project.



## Licensing

The DocBooking backend project, developed by Tatenda Torerwa at AXL Africa in 2024, is licensed under the MIT License, allowing users to freely use, modify, and distribute the software. The MIT License grants permission without warranty and requires the inclusion of the original copyright notice and permission notice in all copies or substantial portions of the software.

