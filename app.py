from flask import Flask, render_template, request, redirect, url_for, flash
import hospital_data

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Required for flashing messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form.get('query')
        hospitals = hospital_data.search_hospitals(query)
        return render_template('search.html', hospitals=hospitals, query=query)
    return render_template('search.html', hospitals=None)

@app.route('/book_doctor/<hospital_name>/<doctor_name>', methods=['GET', 'POST'])
def book_doctor(hospital_name, doctor_name):
    doctor = hospital_data.get_doctor(hospital_name, doctor_name)
    if request.method == 'POST':
        patient_name = request.form.get('patient_name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        contact = request.form.get('contact')
        appointment_date = request.form.get('appointment_date')
        notes = request.form.get('notes')

        # Handle booking logic here

        # Flash confirmation message and render booking details
        flash('Booking successful!', 'success')
        return render_template('booking_confirmation.html', doctor=doctor, patient_name=patient_name, age=age,
                               gender=gender, contact=contact, appointment_date=appointment_date, notes=notes)

    return render_template('book_doctor.html', doctor=doctor)

@app.route('/add_hospital', methods=['GET', 'POST'])
def add_hospital():
    if request.method == 'POST':
        name = request.form.get('name')
        address = request.form.get('address')
        doctors = request.form.get('doctors')
        hospital_data.add_hospital(name, address, doctors)
        return redirect(url_for('index'))
    return render_template('add_hospital.html')

if __name__ == '__main__':
    app.run(debug=True)
