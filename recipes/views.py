from django.http import HttpResponse
from django.shortcuts import render
from . models import Recipe

# Create your views here.

def index(request):
    #recipes = Recipe.objects.all()
    #recipes = Recipe.objects.filter(category = "sallad")  WRONG WAY TO CALL A REFERENCE TO A CATEGORY.
    #recipes = Recipe.objects.filter(category__name__exact = "Pizza") # Good
    #recipes = Recipe.objects.filter(category__name__contains = "pizza") #Good
    recipes = Recipe.objects.exclude(name__contains = "Pot") #Excluding from the query.
    # __ is the DJango ORM syntax. It allows to stand relationship and filter between on fields of related models.
    # The name "name", "category" must be exact the same as the current model.
    print(recipes)
    return HttpResponse("Hello From Recipe!")