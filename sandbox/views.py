from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# Any view has to take a request *
def helloWorld(request):
    return HttpResponse("Hello World! From the ("") path in the urls.py")