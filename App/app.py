# TODO : Clean var ; rem cache
import sms_query as sms
import retreiveData as rd
import time,pickle
from flask import Flask, jsonify,request 

app = Flask(__name__)

'''

ADD TEMPLATE : 

'''

@app.route('/',methods=["GET"])
def query():
    previous = ""
    file = open("./pinToLocMap.pickle","rb")
    placename = pickle.load(file)
    file.close()
    ans,number = sms.response()
    print(ans,number)
    number = str(number)[2:]
    # temp = sms.get_context(ans)
    flag = -1 
    # if temp[-1]==0:
    #     #sms.sendSMS(number,temp[0])
    #     print("SENT :",temp[0])
    #     print("*"*80)
    #     response =  [number,temp[0]]
    #     flag = 0 
    # else:
    #     flag = temp[-1]
    #     response = temp[:-1] 
    # if flag == 2:
    #     data = rd.google_directions(response[0],response[1],response[2])
    #     # sms.sendSMS(number,data)
    #     print("SENT :",data)
    #     print("*"*80)
    # elif flag == 3:
    #     data = rd.process_detail(response[0])
    #     # sms.sendSMS(number,"ADDRESS: \n"+data)
    #     print("SENT :",data)
    #     print("*"*80)
    # elif flag:
    #     pincode = response[0]
    #     query = response[1]
    #     contact = number
    #     # pin code conv .
    #     data = rd.retreive_area(placename[str(pincode)],query)
    #     if len(data) == 1:
    #         # sms.sendSMS(number,data)
    #         print("SENT :",data)
    #         print("*"*80)
    #     elif data != None:
    #         if data[1]!=None:
    #             data = data[0]+"\n"+data[1]+"\n"+data[2]
    #         else:
    #             data = data[0]+"\n"+data[2]
    #         print("SENT :",data)
    #         print("*"*80)
    #         # sms.sendSMS(number,data)
    # print(data)
    print("Message Sent : app.py")

if __name__ == "__main__":
    app.run(debug=True,port=8080)