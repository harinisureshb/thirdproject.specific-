from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def lsg(request):
    return HttpResponse('<h1> RAHUL is the capitan</h1>')

def csk(request):
    return HttpResponse('<h1> MR COOL is the CAPTAIN</h1>')