# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from . import queries
import requests
import googlemaps
from .config import * 


# Create your views here.
def index(request):
    return render(request,'app/map.html')

def appindex(request):
    return render(request,'app/map.html')

def map(request):
    # FSWMCH
    if(request.method == 'POST'):
        # food = request.POST.get('cbx1')
        # shelter = request.POST.get('cbx2')
        # water = request.POST.get('cbx3')
        # medicine = request.POST.get('cbx4')
        # cloth = request.POST.get('cbx5')
        # hygenie = request.POST.get('cbx6')
        fin = []
        for i in range(1,7):
            temp = request.POST.get('cbx'+str(i))
            if temp == 'on':
                fin.append('1')
            else:
                fin.append('0')
        print(fin)
        count=1
        result = queries.find_specific_donors(fin)
        print(result)
        # result = [1,2,3,4]
        return render(request,'app/map.html',{"result": result, "fin":fin})
    else:
        donors = queries.find_donors()
        # print(donors['id'])
        list = []
        for i in donors:
            list.append(donors[i])
        return render(request,'app/map.html',{'list':list})

def retreive_area(lat,lon):
    print("Retreiving data")
    gmaps = googlemaps.Client(key="AIzaSyAwAdfRMQoKv8Tmc4iD2KsDCXQfWoxVJkk")
    reverse_geocode_result = gmaps.reverse_geocode((lat, lon))
    print(reverse_geocode_result)
    return 1
    #key = key.upper()
    # print(loc,key)
    # query_result = google_places.nearby_search(location=loc, keyword=key, radius=2000, types=[type_map[key]])
    # places_data = []        # name,number,addr
    # for place in query_result.places:
    #     # print(place.place_id)
    #     x = place.get_details()
    #     places_data.append([place.name,place.local_phone_number,place.vicinity])
    # if len(places_data):
    #     return places_data[0]

def calamity(request):
    sos = queries.get_sos()
    # r = requests.get("https://api.ipdata.co?api-key="+GLapikey).json()
    #lon,lat = r["longitude"],r["latitude"]
    #details = retreive_area(lat,lon)
    #print(details)
    return render(request,'app/calamity.html',{'list':sos})

def provisions(request):
    temp = queries.get_issue()
    print("//////////////")
    print(temp)
    return render(request,'app/provisions.html',{'src': temp})

def need(request):
    if(request.method == 'POST'):
        fin = []
        for i in range(1,7):
            temp = request.POST.get('cb'+str(i))
            if temp == 'on':
                fin.append('1')
            else:
                fin.append('0')
        print(fin)
        index = queries.number_of_req("donor")
        rd = 0
        fswmch = "".join(fin)
        desc = request.POST.get('descr')
        address = request.POST.get('addr')
        name = request.POST.get('name')
        number = request.POST.get('phn')
        
        queries.add_donors(index,rd,fswmch,desc,address,name,number)
        return render(request,'app/map.html')

def issue(request):
    if(request.method == "POST"):
        index = queries.number_of_req("issues")
        name = request.POST.get("name")
        descr = request.POST.get("descr")
        date = request.POST.get("date")
        dept = request.POST.get("dept")
        print(name,descr,date,dept)
        queries.add_issue(descr,name,dept,date)
    return render(request, 'app/map.html')

# def adddonors(request):
#     if(request.method == 'POST'):
#         name = request.POST.get('name')
#         dob = request.POST.get('dob')
#         state = request.POST.get('state')
#         district = request.POST.get('district')
#         block = request.POST.get('block')
#         pincode = request.POST.get('pincode')
#         phone = request.POST.get('phone')
#         temp = request.POST.getlist('checks[]')
#         #data = Crop.objects.filter(region=pincode)[0]
#         #x = Farmer(name=name,dob=dob,state=state,district=district,block=block,pincode=pincode,phone=phone,crops=crops,data=data)
#         #x.save()
#         #u = reverse('app:dashboard',kwargs={'username':str(request.user)})
#         #print(str(request.user))
#         #return HttpResponseRedirect(u)
#     else:
#         #return render(request,'app/farmer.html',{})
