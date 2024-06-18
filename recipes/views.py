from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpRequest("Hello From Recipe!")