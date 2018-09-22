# TODO : Clean var ; rem cache
import query  
import retreiveData as retreive
import time,pickle
from flask import Flask, jsonify,redirect, url_for, request
import json,re
import urllib
import pyrebase
from config import email,password,config

firebase = pyrebase.initialize_app(config)
auth=firebase.auth()
user=auth.sign_in_with_email_and_password(email,password)

def refresh(user):
    user=auth.refresh(user['refreshToken'])

db = firebase.database()


app = Flask(__name__)
counter = 1

'''
ADD TEMPLATE : 

1 =========
emergency <fire/police/hospital>
Addr
Addr [opt]

2 =========
requirement <cloth/food/>
Addr
Addr [opt]


3 =========

4 =========


5 =========



'''


@app.route('/',methods = ['POST', 'GET'])
def user_query():
    if request.method == 'POST':
        global counter
        data = request.get_data()
        result = data.decode("utf-8")

        result = result[:result.index("inNumber")-1]
        sender,message = result[:result.index('&')],result[result.index('&')+1:]
        sender = sender.split("=")[1][2:]
        message = message.split("=")[1]

        lines = message.split("%0A")
        sentence = ""
        for line in lines[1:]:
            sentence +=  " ".join(line.split("%20")) + " \n"
        
        # Get Pincode To Location Mapping
        pkfile = open("./pinToLocMap.pickle","rb")
        placename = pickle.load(pkfile)
        pkfile.close()

        print(sentence)
        query_dict = query.apiai_query(sentence)
        response_type = None

        if query_dict[-1] == 0:
            query.sendSMS(sender,query_dict[0])
            print("SENT :",query_dict[0])
            print("*"*80)
            response_type = 0 

        else:
            response_type = query_dict[-1]
            response = query_dict[:-1]
        
        if response_type == 2:
            data = retreive.google_directions(response[0],response[1],response[2])
            query.sendSMS(sender,data)
            print("SENT :",data)
            print("*"*80)

        elif response_type == 3:
            data = retreive.process_detail(response[0])
            query.sendSMS(sender,"ADDRESS: \n"+data)
            print("SENT :",data)
            print("*"*80)

        elif response_type == 1:
            pincode = response[0]
            query_i = response[1]

            # pin code conv .
            data = retreive.retreive_area(placename[str(pincode)],query_i)
            if len(data) == 1:
                query.sendSMS(sender,data)
                print("SENT :",data)
                print("*"*80)
            elif data != None:
                if data[1]!=None:
                    data = data[0]+"\n"+data[1]+"\n"+data[2]
                else:
                    data = data[0]+"\n"+data[2]
                print("SENT :",data)
                print("*"*80)
                query.sendSMS(sender,data)
        elif response_type == 4:
            response.append(sender)
            
            donor=db.child("announce").get(user['idToken']).val()
            donor["x"+str(counter)]=response
            db.child("announce").set(donor,user['idToken'])
            
            counter += 1
            data = retreive.retreive_area(response[1],response[-2])
            
            if len(data) == 1:
                query.sendSMS(sender,data)
                print("SENT :",data)
                print("*"*80)
            elif data != None:
                if data[1]!=None:
                    data = data[0]+"\n"+data[1]+"\n"+data[2]
                else:
                    data = data[0]+"\n"+data[2]
                print("SENT :",data)
                print("*"*80)
                query.sendSMS(sender,data)
        elif response_type == 5:
            response.insert(5,sender)
            message = "Your requirement has been registered! Thanks"
            donor=db.child("donor").get(user['idToken']).val()

            print(response)
            donor["x"+str(counter)]=response
            db.child("donor").set(donor,user['idToken'])
            
            counter += 1
            query.sendSMS(sender,message)
            print("DONE!")
            
        print("Message Sent : app.py")

        return "POST REQUEST"
    else:
        return "GET REQUEST"

if __name__ == "__main__":
    app.run(debug=True,port=8080)