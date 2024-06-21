from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView

from recipes.models import Recipe
from sandbox.forms import FeedbackForm

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

def feedback(request):
    if(request.method == "POST"):
        form = FeedbackForm(request.POST)
        if(form.is_valid()):
            print(form.cleaned_data)
            return redirect("sandbox:thankYou") #thankYou is the name of the path (in the urls.py) to thank_you view
    else:
        form = FeedbackForm()
        context = {"form": form}
        return render(request, "sandbox/feedback_form.html", context=context)



def thank_you(request):
    return HttpResponse("Thanks You for your feedback")


# Class Based View (much better for reuseability) (A Generic Class)
class RecipeListView(ListView):
    model = Recipe
    template_name = "sandbox/sandbox.html"
    context_object_name = "recipes"
    # For filtering between objects, we can override query functions.
    def get_queryset(self):
        filtered_recipes = Recipe.objects.filter(category__name__iexact="Salad")
        return filtered_recipes
    
# Custom class-based view
class SpecificRecipeView(View):
    def get(self, request, *args, **kwargs):
        #Fetch Recipe 
        refreshing_recipes = Recipe.objects.filter(description__icontains = "refreshing")
        #Pass through a context
        context = {"refreshing":refreshing_recipes}
        #Returning
        return render(request, 'sandbox/refreshing_recipes.html', context)
