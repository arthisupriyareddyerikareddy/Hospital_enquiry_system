
# Hospital Enquiry System

## Overview

The **Hospital Enquiry System** is a web-based application that allows users to search for hospitals, view doctors, and book appointments directly through the interface. The project provides a user-friendly experience with dynamic hospital and doctor details, including features like booking confirmation and flash messages.

## Features

- **Search Hospitals**: Users can search for hospitals based on a query.
- **View Doctor Details**: View detailed information about available doctors at different hospitals.
- **Book Doctor Appointments**: Allows users to book appointments with a doctor by filling out their details.
- **Responsive UI**: Designed with a cinematic and dynamic interface, including glassmorphism effects and background animations.
- **Flash Messages**: Confirms successful bookings using flash messages.

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: (Optional) You can integrate with a database like SQLite or PostgreSQL.
- **Styling**: CSS animations, flexbox, and grid for responsiveness.
- **Icons**: FontAwesome for animated icons (optional, can be added for a dynamic experience).

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- Flask (`pip install flask`)
- Fast API

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/hospital-enquiry-system.git
   cd hospital-enquiry-system
   ```

2. Set up a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app:
   ```bash
   python app.py
   ```

5. Open your browser and go to `http://127.0.0.1:5000/` to view the application.

## Project Structure

```
hospital-enquiry-system/
│
├── app.py                     # Main Flask application
├── hospital_data.py            # Data handling (hospital and doctor info)
├── static/
│   ├── styles.css              # CSS styles
│   ├── hospital_bg.jpg         # Background image
│   └── ...
├── templates/
│   ├── index.html              # Main HTML page
│   ├── search.html             # Search results page
│   ├── book_doctor.html        # Doctor booking page
│   └── booking_confirmation.html # Booking confirmation page
├── README.md                   # Project documentation
└── requirements.txt            # Python dependencies
```

## Usage

1. **Home Page**: Start by visiting the homepage where you can search for hospitals.
2. **Search**: Enter a query in the search bar, and the system will display a list of hospitals matching the search.
3. **Book Appointment**: Click on a hospital to view doctors and book an appointment by filling out the form.
4. **Confirmation**: After booking, you’ll receive a confirmation with the doctor’s and your details.

## Sample Data

The project includes some sample data for hospitals and doctors in `hospital_data.py`. You can modify this data to fit real-world use cases or connect to a database.

Example:
```python
def get_hospitals():
    return [
        {
            'name': 'City Hospital',
            'price': '$200',
            'location': 'New York, NY',
            'availability': 'Monday - Friday, 9am - 5pm',
            'contact': '123-456-7890',
            'doctor_name': 'Dr. Smith'
        },
        ...
    ]
```

## Screenshots

### Homepage
![Homepage](static/hospital_bg.jpg)

### Search Results
A list of hospitals based on the query.

### Book Doctor
A detailed view of the selected doctor along with a booking form.

## Future Enhancements

- **Database Integration**: Use a database like SQLite or PostgreSQL for persistent hospital and doctor data.
- **User Authentication**: Add login and registration functionality.
- **Appointment History**: Allow users to view their past and upcoming appointments.
- **Google Maps Integration**: Show hospital locations on a map.

## License

This project is licensed under the MIT License.


