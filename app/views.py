from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hari(request,name):
    return HttpResponse(f'welcome to my world {name}')