import urllib.request
import urllib.parse
import codecs
import json,re
from config import *


ccess_token = "" # Enter your Access Token here
client=apiai.ApiAI(Access_token)

def apiai_query(message):
    req=client.text_request()
    req.lang="de"
    req.session_id="<SESSION ID, UNIQUE FOR EACH USER>"
    req.query=message
    response=json.loads(req.getresponse().read().decode('utf-8'))
    responseStatus = response['status']['code']
    if responseStatus==200 :
        text = response['result']['fulfillment']['speech']
    else:
        text="No Match Found"
    result=response["result"]
    param=result["parameters"]
    if len(param.keys())==0:
        return [text,0]
    if "number" in param.keys():
        pin=param["number"]
    if "tof" in param.keys():
        tof=param["tof"]
    if "type" in param.keys():
        typ=param["type"]
        if typ=="routes":
            message=message.split("\n")
            if(len(message)>3):
                mod=message[3]
            else:
                mod='transit'
            return [message[1],message[2],mod,2]
        elif typ=="detail":
            message=message.split('\n')[1:]
            print(("*"*30)+"  DETAILED LOCATION  " + "*"*30)
            message = ",".join(message)
            print("RECEIVED : ",message)
            return [message,3]
        elif typ=="nearby":
            return [pin,tof,typ,1]

def getMessages(inboxID):
    data =  urllib.parse.urlencode({'apikey': TLapikey, 'inbox_id' : inboxID})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/get_messages/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)

def sendSMS(number, message):
    data =  urllib.parse.urlencode({'apikey': TLapikey, 'numbers': number,
        'message' : message})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data[:min(len(data),740)])
    fr = f.read()
    print("MESSAGE SENT")

def response():
    resp = getMessages('10')
    ans = json.loads(resp.decode('ASCII'))
    message = ans["messages"][-1]["message"][6:]
    sender = ans["messages"][-1]["number"]
    return ans
    #return message,sender

if __name__ == "__main__":
    # sendSMS("7045185177","HEY")
    print(response())
