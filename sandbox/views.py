from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from recipes.models import Recipe

# Create your views here.

# Any view has to take a request *
def helloWorld(request):
    return HttpResponse("Hello World! From the ("") path in the urls.py")

# function-based view
def index(request):
    # A view for dynamically calling the index.html
    pageInfo = {"name": "Foodie", "age": 12}
    foods = ['Pizza', 'Sallad', 'Pasta', 'Hamburger', 'Rice']
    context = {
        "pageInfo": pageInfo,
        "foods": foods}
    
    return render(
        request, 
        "sandbox/sandbox.html", 
        context=context )

# Class Based View (much better for reuseability)
class RecipeListView(ListView):
    model = Recipe
    template_name = "sandbox/sandbox.html"
    context_object_name = "recipes"