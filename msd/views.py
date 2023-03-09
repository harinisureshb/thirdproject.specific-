from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def dhoni(request):
    return HttpResponse('<h1>MR COOL</h1>')

def virat(request):
    return HttpResponse('<h2> GOOD CRIKETER </h2>')