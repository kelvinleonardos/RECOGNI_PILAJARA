import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Inisialisasi Firebase Admin SDK dengan credential
cred = credentials.Certificate('realtime-attendance-d815d-firebase-adminsdk-z360g-1679befee6.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://realtime-attendance-d815d-default-rtdb.firebaseio.com/'
})


def up(info, id):
    # Mendapatkan referensi database
    ref = db.reference(f'Students/{id}')

    # Menambahkan value baru ke data
    new_data = info
    ref.push(new_data)
