from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# Any view has to take a request *
def helloWorld(request):
    return HttpResponse("Hello World! From the ("") path in the urls.py")

def index(request):
    # A view for dynamically calling the index.html
    diction = {"name": "Foodie", "age": 12}
    context = {"data": diction}
    return render(
        request, 
        "sandbox/index.html", 
        context=context )