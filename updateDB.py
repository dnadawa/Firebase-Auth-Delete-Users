import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
collection =  db.collection('parking')
docs = collection.get()

count = 0
for i in docs:
    doc = i.to_dict()
    id = i.id
    if "extended" in doc.keys():
        count+=1
    else:
        db.collection('parking').document(id).update({'extended': False})
    print(id)

#display 
print()
print(len(docs) - count, "rows updated")
print(count,"rows already updated")
print("Total: ",len(docs))
