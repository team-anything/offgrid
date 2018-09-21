import requests
from config import * 

r = requests.get("https://api.ipdata.co?api-key="+GLapikey).json()
print(r)

import way2sms
username = "9820501130"
password = "E689N"
q=way2sms.sms(username,password)

