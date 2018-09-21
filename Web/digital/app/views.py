# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request,'app/index.html')

def appindex(request):
    return render(request,'app/appindex.html')

def map(request):
    return render(request,'app/map.html')

def calamity(request):
    return render(request,'app/calamity.html')

def provisions(request):
    return render(request,'app/provisions.html')