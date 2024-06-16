from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def helloWorld():
    return HttpResponse("Hello World! From the ("") path in the urls.py")