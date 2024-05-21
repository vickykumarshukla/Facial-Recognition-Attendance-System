import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-b6317-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "1": {
        "name": "Vicky Shukla",
        "major": "CSE",
        "starting_year": 2021,
        "total_attendance": 40,
        "standing": "Good",
        "year": 4,
        "last_attendance_time": "2023-06-12 09:20:34"
    },
"2": {
        "name": "Elon Musk",
        "major": "Physics",
        "starting_year": 2021,
        "total_attendance": 40,
        "standing": "Good",
        "year": 2,
        "last_attendance_time": "2023-06-12 09:20:34"
    },
"3": {
        "name": "Emly Blunt",
        "major": "Economics ",
        "starting_year": 2021,
        "total_attendance": 60,
        "standing": "Good",
        "year": 1,
        "last_attendance_time": "2023-06-12 09:20:34"
    },
"4": {
        "name": "Narendra Modi",
        "major": "CSE",
        "starting_year": 2021,
        "total_attendance": 80,
        "standing": "Good",
        "year": 3,
        "last_attendance_time": "2023-06-12 09:20:34"
    },
"5": {
        "name": "Pramod Patel",
        "major": "CSE",
        "starting_year": 2021,
        "total_attendance": 22,
        "standing": "Good",
        "year": 3,
        "last_attendance_time": "2023-06-12 09:20:34"
    },
"6": {
        "name": "Robert Downey Junior",
        "major": "CSE",
        "starting_year": 2021,
        "total_attendance": 40,
        "standing": "Good",
        "year": 2,
        "last_attendance_time": "2023-06-12 09:20:34"
    },
"7": {
        "name": "Shivam Shukla",
        "major": "CSE",
        "starting_year": 2022,
        "total_attendance": 40,
        "standing": "Good",
        "year": 3,
        "last_attendance_time": "2023-06-12 09:20:34"
    },
"8": {
        "name": "Piyush Gupta",
        "major": "CSE",
        "starting_year": 2021,
        "total_attendance": 60,
        "standing": "Good",
        "year": 4,
        "last_attendance_time": "2023-06-12 09:20:34"
    },
"9": {
        "name": "Roopam Saha",
        "major": "CSE",
        "starting_year": 2024,
        "total_attendance": 50,
        "standing": "Good",
        "year": 1,
        "last_attendance_time": "2023-06-12 09:20:34"
    },
"10": {
        "name": "Subrat Kumar",
        "major": "CSE",
        "starting_year": 2021,
        "total_attendance": 40,
        "standing": "Good",
        "year": 4,
        "last_attendance_time": "2023-06-12 09:20:34"
    },
"11": {
        "name": "Vikash Rana",
        "major": "CSE",
        "starting_year": 2021,
        "total_attendance": 65,
        "standing": "Good",
        "year": 4,
        "last_attendance_time": "2023-06-12 09:20:34"
    },
"12": {
        "name": "Vikash Saw",
        "major": "CSE",
        "starting_year": 2021,
        "total_attendance": 20,
        "standing": "Good",
        "year": 4,
        "last_attendance_time": "2023-06-12 09:20:34"
    }

}

for key, value in data.items():
    ref.child(key).set(value)
