from googleplaces import GooglePlaces, types, lang
import sys
from config import *
import googlemaps,re
from datetime import datetime


YOUR_API_KEY = GCPapikey # Enter your API Key

google_places = GooglePlaces(YOUR_API_KEY)
gmaps = googlemaps.Client(key=GCPapikey) # Enter your Key here.

type_map = {
    "HOSPITAL":types.TYPE_HOSPITAL,
    "CHEMIST":types.TYPE_PHARMACY,
    "POLICE":types.TYPE_POLICE,
    "TRAIN":types.TYPE_TRAIN_STATION,
    "TAXI":types.TYPE_TAXI_STAND,
    "GAS":types.TYPE_GAS_STATION,
    "ATM":types.TYPE_ATM,
    "BUS":types.TYPE_BUS_STATION,
    "FIRE":types.TYPE_FIRE_STATION,
    }

'''
# TEXT_SEARCH
query_result = google_places.text_search(query="Restaurant in Dahisar",location="Mumbai,India",radius=2000)
'''
def process_detail(key):
    # AUTOCOMPLETE
    query_result = google_places.autocomplete(input=key,location="India",radius=200)
    print(query_result)
    if len(query_result.predictions):
        pred = query_result.predictions[0]
        addr = pred.description
        return addr


# print(dir(types))
# NEARBY AREA SEARCH

def google_directions(ori, dest, mode):
    message = []
    
    now = datetime.now()
    directions_result = None
    try: 
        print(ori,dest,mode)
        print(now)
        directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="driving", departure_time = now)
    except:
        print("A network error occurred; please try again")
    
    if directions_result == None:
        print("An error occurred; please check your inputs and try again")
    message.append("Start from: " + directions_result[0]['legs'][0]['start_address'])
    message.append("End at: " + directions_result[0]['legs'][0]['end_address'])
    message.append("Duration: " + directions_result[0]['legs'][0]['duration']['text'])
    message.append("Distance: " + directions_result[0]['legs'][0]['distance']['text'])
    
    regex = re.compile('<[^>]*>')
    style_regex = re.compile('<[^>]*(style)[^>]*>')
    for each in directions_result[0]['legs'][0]['steps']:
        instr = re.sub(style_regex, '; ', each['html_instructions'])
        instr = re.sub(regex, '', instr)
        message.append(instr)
    return '\n'.join(message)


def retreive_area(loc,key):
    print("Retreiving data")
    key = key.upper()
    print(loc,key)
    query_result = google_places.nearby_search(location=loc, keyword=key, radius=2000, types=[type_map[key]])
    places_data = []        # name,number,addr
    for place in query_result.places:
        # print(place.place_id)
        x = place.get_details()
        places_data.append([place.name,place.local_phone_number,place.vicinity])
    if len(places_data):
        return places_data[0]

def latlong(addr):
    geocode_result = gmaps.geocode(addr)
    latlng=geocode_result[0]['geometry']['location']
    return [latlng['lat'],latlng['lng']]
    
if __name__ == "__main__":
    # print(retreive_area(loc="Dahisar ,Mumbai",key="POLICE"))
    print(google_directions('sec10 Airoli', 'Somaiya VidyaVihar', 'driving'))
    #print(google_directions)
    #print(process_detail('KJSCE ,VidyaVihar'))
    print(retreive_area('KJSCE ,VidyaVihar',"fire"))
