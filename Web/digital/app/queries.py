import pyrebase
from .config import config,email,password

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

def find_specific_donors(queue):
    refresh(user)
    donors=db.child("donor").get(user["idToken"]).val()
    results=[]
    queue=int("".join(queue),2)
    for key in donors.keys():
        if int(donors[key][1],2) & queue:
            results.append(donors[key])
    return 


def add_donors(id,rd,fswmch,name,descr,address,number):
    refresh(user)
    donor=db.child("donor").get(user['idToken']).val()
    id = str(id)
    print([rd,fswmch,name,descr,number,address])
    # donor[id]=[rd,fswmch,cords,name,descr,number,address]
    # db.child("donor").set(donor,user['idToken'])

def number_of_req():
    refresh(user)
    donor=db.child("donor").get(user["idToken"]).val()
    return len(donor)


    