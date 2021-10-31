import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
collection =  db.collection('parking')
docs = collection.get()



for i in docs:
    doc = i.to_dict()
    id = i.id
    db.collection('parking').document(id).update({'extended': False})
    print(id)
