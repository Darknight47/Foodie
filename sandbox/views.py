from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# Any view has to take a request *
def helloWorld(request):
    return HttpResponse("Hello World! From the ("") path in the urls.py")

def index(request):
    # A view for dynamically calling the index.html
    pageInfo = {"name": "Foodie", "age": 12}
    foods = ['Pizza', 'Sallad', 'Pasta', 'Hamburger', 'Rice']
    context = {
        "pageInfo": pageInfo,
        "foods": foods}
    
    return render(
        request, 
        "sandbox/index.html", 
        context=context )