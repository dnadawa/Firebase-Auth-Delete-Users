import firebase_admin
from firebase_admin import credentials, auth

# Use a service account
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)

users = []

for user in auth.list_users().iterate_all():
    #only delte anonymous users who doesnt have an email
    if(user.email==None):
        users.append(user.uid)

result = auth.delete_users(users)
print('Successfully deleted {0} users'.format(result.success_count))
print('Failed to delete {0} users'.format(result.failure_count))
for err in result.errors:
    print('error #{0}, reason: {1}'.format(result.index, result.reason))