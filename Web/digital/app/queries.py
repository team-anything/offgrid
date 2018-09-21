import pyrebase

config={
        "apiKey": "AIzaSyAbR4GEnADyWeqqIr9BHQ6NbgWoGQ2U8lA",
        "authDomain": "digizen-8527d.firebaseapp.com",
        "databaseURL": "https://digizen-8527d.firebaseio.com",
        "storageBucket": "digizen-8527d.appspot.com"
}

email="teamanything98@gmail.com"
password="testing1234"

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
    main=db.get(user['idToken']).val()
    donor={}
    donor[id]=[rd,fswmch,latlong,number,address]
    main["donor"]=donor
    db.set(main,user['idToken'])


    