# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from . import queries


# Create your views here.
def index(request):
    return render(request,'app/index.html')

def appindex(request):
    return render(request,'app/appindex.html')

def map(request):
    if(request.method == 'POST'):
        food = request.POST.get('prov1')
        shelter = request.POST.get('prov2')
        lat = request.POST.get('prov3')
        lng = request.POST.get('prov1')
        number = request.POST.get('prov1')
        address = request.POST.get('prov1')
        count=1
        queries.add_donors(str(count),food,shelter,[lat,lng],number,address)
        return render(request,'app/map.html')
    else:
        donors = queries.find_donors()
        #print(donors['id'])
        list = []
        for i in donors:
            list.append(donors[i])
        return render(request,'app/map.html',{'list':list})

def calamity(request):
    return render(request,'app/calamity.html')

def provisions(request):
    return render(request,'app/provisions.html')


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
