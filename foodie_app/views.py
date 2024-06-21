from django.shortcuts import render

from foodie_app.forms import CategoryForm
from . models import Category
from recipes.models import Recipe

# Create your views here.
def index(request):
    #Inside the foodie_app execute the index.html
    categories = Category.objects.all()
    context = {"categories": categories}

    return render(request, "foodie_app/index.html", context=context)


def catRecipes(request, category_id):
    recipies = Recipe.objects.filter(category=category_id)
    category = Category.objects.get(id=category_id)
    context = {'catRecipes': recipies,
               'category': category}
    
    return render(request, "foodie_app/catrecipes.html", context=context)

def add_category(request):
    form = CategoryForm()
    context = {"form": form}
    return render(request, "foodie_app/add_category.html", context)