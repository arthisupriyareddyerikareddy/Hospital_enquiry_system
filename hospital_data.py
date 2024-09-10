# Simulating a database of hospitals and doctors
hospitals = [
    {
        "name": "City Hospital",
        "address": "123 Main St",
        "doctors": [
            {
                "name": "Dr. John Smith",
                "specialty": "Cardiologist",
                "price": "$150",
                "location": "Room 101",
                "availability": "9:00 AM - 5:00 PM",
                "contact": "123-456-7890"
            },
            {
                "name": "Dr. Emily Rose",
                "specialty": "Dermatologist",
                "price": "$120",
                "location": "Room 102",
                "availability": "10:00 AM - 6:00 PM",
                "contact": "123-555-7890"
            }
        ]
    },
    {
        "name": "Green Valley Hospital",
        "address": "456 Oak St",
        "doctors": [
            {
                "name": "Dr. Michael Davis",
                "specialty": "Neurologist",
                "price": "$200",
                "location": "Room 201",
                "availability": "11:00 AM - 7:00 PM",
                "contact": "456-789-1234"
            }
        ]
    }
]

def add_hospital(name, address, doctors):
    hospital = {
        'name': name,
        'address': address,
        'doctors': doctors
    }
    hospitals.append(hospital)

def search_hospitals(query):
    return [hospital for hospital in hospitals if query.lower() in hospital['name'].lower()]

def get_doctor(hospital_name, doctor_name):
    for hospital in hospitals:
        if hospital['name'] == hospital_name:
            for doctor in hospital['doctors']:
                if doctor['name'] == doctor_name:
                    return doctor
    return None
