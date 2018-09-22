import pyrebase
import googlemaps
from .config import config,email,password,GCPapikey

firebase = pyrebase.initialize_app(config)
auth=firebase.auth()
user=auth.sign_in_with_email_and_password(email,password)

gmaps = googlemaps.Client(key=GCPapikey)


def refresh(user):
    user=auth.refresh(user['refreshToken'])

db=firebase.database()

def latlong(addr):
    geocode_result = gmaps.geocode(addr)
    latlng=geocode_result[0]['geometry']['location']
    return [latlng['lat'],latlng['lng']]

def find_donors():
    refresh(user)
    donors=db.child("donor").get(user['idToken']).val() #retrieve a last of values
    return donors

def find_specific_donors(queue):
    refresh(user)
    donors=db.child("donor").get(user["idToken"]).val()
    results=[]
    queue=int("".join(queue),2)
    for key in donors.keys():
        if int(donors[key][1],2) & queue:
            results.append(donors[key])
    return results


def add_donors(id,rd,fswmch,desc,address,name,number):
    refresh(user)
    donor=db.child("donor").get(user['idToken']).val()
    id = str(id)
    #print("******")
    cords=latlong(address)
    #print([rd,fswmch,cords,name,desc,number,address])
    donor[id]=[rd,fswmch,cords,name,desc,number,address]
    db.child("donor").set(donor,user['idToken'])

def number_of_req(x):
    refresh(user)
    donor=db.child(x).get(user["idToken"]).val()
    return len(donor)


    