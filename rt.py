import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Inisialisasi Firebase Admin SDK dengan credential
cred = credentials.Certificate('realtime-attendance-d815d-firebase-adminsdk-z360g-1679befee6.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://realtime-attendance-d815d-default-rtdb.firebaseio.com/'
})

# Referensi ke Firebase Realtime Database
ref = db.reference('cobacoba')

# Tambahkan data baru ke Firebase Realtime Database
data = {
    "321654":
        {
            "name": "Murtaza Hassan",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)

print('Data baru berhasil ditambahkan ke Firebase Realtime Database!')