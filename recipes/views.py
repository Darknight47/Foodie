from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from foodie_app.forms import RecipeForm
from foodie_app.models import Category
from . models import Recipe
from django.db.models import Sum, Count
from django.db.models import Q # Complex Queries

# Create your views here.

def index(request):
    """
        recipes = Recipe.objects.all()
        recipes = Recipe.objects.filter(category = "sallad")  WRONG WAY TO CALL A REFERENCE TO A CATEGORY.
        recipes = Recipe.objects.filter(category__name__exact = "Pizza") # Good
        recipes = Recipe.objects.filter(category__name__contains = "pizza") #Good
        recipes = Recipe.objects.exclude(name__contains = "Pot") #Excluding from the query.
        __ is the DJango ORM syntax. It allows to stand relationship and filter between on fields of related models.
        The name "name", "category" must be exact the same as the current model.
        
        Chaining the queries.
        rderedRecipes = (
            Recipe.objects.filter(category__name__icontains = "pizza")
            .exclude(name__icontains = "mar")
            .order_by("-date_added") # Descending Order "-", without it ascending order.
        )

        Two first objects
        twoFirstRecipes = Recipe.objects.all()[:2]

        Aggregating objects
        amountOfRecipes = Recipe.objects.aggregate(Count("name")) #Count("NAME OF A FIELD")

        specialRecipe = Recipe.objects.filter(Q(name__startswith="M") | Q(description__contains="salt")) # | OR
        print(orderedRecipes)
        print(amountOfRecipes)
        print(specialRecipe)
    """
    
    recipes = Recipe.objects.all() # Getting all the recipes
    context = {"recipes": recipes} # key: recipes, the key is going to be called in the index.html

    return render(request, "recipes/index.html", context=context)

def recipeView(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    context = {"recipe": recipe}
    return render(request, "recipes/recipe.html", context=context)

# Adding a recipe when we already are inside a specific category.
def add_recipe(request, category_id=None):
    category = None
    if(category_id):
        #category = Category.objects.get(id=category_id)
        category = get_object_or_404(Category, id=category_id) #A safer way to get an object from the DB!
        form = RecipeForm(request.POST or None, initial={"category": category})
    else:
        form = RecipeForm(request.POST or None)
    
    if(request.method == "POST" and form.is_valid()):
        new_recipe = form.save()
        return redirect("foodie_app:cat_recipes", category_id=new_recipe.category.id)
    
    context = {"form": form, "category": category}
    return render(request, "recipes/add_recipe.html", context=context)
