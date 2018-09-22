import urllib.request
import urllib.parse
import codecs
import json,re
from config import *
import apiai
import retreiveData as retreive

client=apiai.ApiAI(APIAIKey)

need_list = ["food","shelter","water","medicine","cloth","hygene"]

def apiai_query(message):
    req=client.text_request()
    req.lang="de"
    req.session_id="<SESSION ID, UNIQUE FOR EACH USER>"
    req.query=message

    response=json.loads(req.getresponse().read().decode('utf-8'))
    responseStatus = response['status']['code']

    print(response)

    if responseStatus == 200 :
        text = response['result']['fulfillment']['speech']
    else:
        text="No Match Found"

    result=response["result"]
    param=result["parameters"]
    if len(param.keys())==0:
        return [text,0]
    if "number" in param.keys():
        pin_code = param["number"]
    if "department" in param.keys():
        department = param["department"][0]
    if "type" in param.keys():
        typ = param["type"][0]
        if typ == "route":
            message = message.split("\n")
            if ( len(message)>3 ) :
                mode = message[3] 
            else:
                mode = 'transit'
            print([message[1],message[2],mode,2])
            return [message[1],message[2],mode,2]
        elif typ == "complete":
            message = message.split('\n')[1:]
            print(("*"*30)+"  DETAILED LOCATION  " + "*"*30)
            message = ",".join(message)
            print("RECEIVED : ",message)
            return [message,3]
        elif typ=="nearby":
            return [pin_code,department,typ,1]
        elif typ=="emergency":
            message = message.split('\n')
            description = message[0]
            message = message[1:]
            message = ",".join(message)
            print(message)
            actual_addr = retreive.process_detail(message)
            print(actual_addr)

            return [description,actual_addr,department,4]
        elif typ=="requirement":
            x = ["0"]*6
            x[need_list.index(department)] = "1"
            x = "".join(x)
            message = message.split('\n')
            description = message[0]
            message = message[1:]
            message = ",".join(message)
            actual_addr = retreive.process_detail(message)
            lat_long = retreive.latlong(actual_addr)

            return [0,x,lat_long,"N/A",description,actual_addr,5]
            
    print("REACHED END")

def sendSMS(number, message):
    data =  urllib.parse.urlencode({'apikey': TLapikey, 'numbers': number,
        'message' : message})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data[:min(len(data),740)])
    fr = f.read()
    print("MESSAGE SENT")

if __name__ == "__main__":
    # sendSMS("7045185177","HEY")
#     print(apiai_query('''complete address 
# sheffield apartments
# dahisar'''))
    print(apiai_query('''emergency fire at 
sheffield apartments
dahisar'''))
