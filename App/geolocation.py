import requests
from config import * 

r = requests.get("https://api.ipdata.co?api-key="+GLapikey).json()
print(r)
