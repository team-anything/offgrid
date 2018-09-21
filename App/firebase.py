import pyrebase
from config import email,password,config

firebase = pyrebase.initialize_app(config)
auth=firebase.auth()
user=auth.sign_in_with_email_and_password(email,password)

def refresh(user):
    user=auth.refresh(user['refreshToken'])

db=firebase.database()

lis=[]
#a={"testing":[1,2,3,4,5,6]}
#lis.append(a)
announce=db.child("announce").get(user['idToken']).val() #retrieve a last of values
donor=db.child("donor").get(user['idToken']).val()
print(donor)
donor["id"]=["r/d","f/s/w/m/c/h",["lat","long"],"number","address"]
db.child("donor").set(donor,user['idToken'])
#announce["shivam"]=["shivam","pawase",10]
#db.child("announce").set(announce,user['idToken'])
#db.child("user").child("testing").set(sender_id,user['idToken']) #add dictionary value {testing:sender_id}
#db.child('Ulist').set(lis,user['idToken'])#add a list
#articles_per_source = db.child("sources").get(user['idToken']).val() #retrieve a last of values