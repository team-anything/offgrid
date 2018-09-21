import urllib.request
import urllib.parse
import codecs
import json,re
from config import *

def apiai_query():
    print("YAY")

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
