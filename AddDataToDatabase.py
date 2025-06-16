import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize Firebase app with service account credentials
cred = credentials.Certificate("Graduation-Project.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://graduation-project-b2bae-default-rtdb.firebaseio.com/",
})

# Get a reference to the 'Students' node
ref = db.reference('Students')

# Sample student data
data = {
    "89922": {
        "name": "Mohammed Belal ",
        "major": "Communication",
        "starting_year": 2019,
        "total_attendance": 3,
        "Phase": "D",
        "last_attendance_time": "2024-4-17 12:00:00"
    },
    "89921": {
        "name": "Omar Khalid",
        "major": "Communication",
        "starting_year": 2019,
        "total_attendance": 3,
        "Phase": "D",
        "last_attendance_time": "2024-4-10 12:00:00"

   },
    "99999": {
        "name": "Vin Diesel",
        "major": "Mechanical Engineering",
        "starting_year": 2019,
        "total_attendance": 5,
        "phase": "C",
        "last_attendance_time": "2024-4-17 12:00:00"

    },
    "89924": {
        "name": "Jason Statham",
        "major": "Bio Engineering",
        "starting_year": 2018,
        "total_attendance": 0,
        "phase": "C",
        "last_attendance_time": "2024-4-28 12:00:00"

    },

}



# Loop through the data and set it in the database
for key, value in data.items():
    ref.child(key).set(value)
