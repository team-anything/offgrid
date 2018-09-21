import pyrebase
from App.config import config,email,password

firebase = pyrebase.initialize_app(config)
auth=firebase.auth()
user=auth.sign_in_with_email_and_password(email,password)

def refresh(user):
    user=auth.refresh(user['refreshToken'])

db=firebase.database()

def find_donors():
    refresh(user)
    donors=db.child("donor").get(user['idToken']).val() #retrieve a last of values
    return donors

def add_donors(id,rd,fswmch,latlong,number,address):
    refresh(user)
    announce=db.child("announce").get(user['idToken']).val() #retrieve a last of values
    donor=db.child("donor").get(user['idToken']).val()
    donor[id]=[rd,fswmch,latlong,number,address]
    db.child("donor").set(donor,user['idToken'])


    