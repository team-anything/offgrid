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
        # result = [1,2,3,4]
        print(result)
        return render(request,'app/map.html',{"result": result, "fin":fin})
    else:
        donors = queries.find_donors()
        # print(donors['id'])
        list = []
        for i in donors:
            list.append(donors[i])
        return render(request,'app/map.html',{'list':list})

def calamity(request):
    return render(request,'app/calamity.html')

def provisions(request):
    temp = ["AAAAA","CCCCCCC","DDDDDDDDDD","XXXXXXXXXXX"]
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
        index = queries.number_of_req()
        final = [index,0]
        final.append("".join(fin))
        final.append(request.POST.get("name"))
        final.append(request.POST.get("descr"))
        final.append(request.POST.get("addr"))
        final.append(request.POST.get("phn"))
        
        queries.add_donors(final[0],0,final[1],final[2],final[3],final[4],final[5])
        print(final)
        # result = [1,2,3,4]
        return render(request,'app/map.html')

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
