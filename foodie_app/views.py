from django.shortcuts import get_object_or_404, render, redirect

from foodie_app.forms import CategoryForm, RecipeForm
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
    #request by default is get
    print(request)
    if(request.method == "POST"):
        form = CategoryForm(request.POST)
        if(form.is_valid()):
            form.save()
            #return render(request, "foodie_app/index.html")
            return redirect("foodie_app:index") #Redirect to the first path of this app.
        else:
            return render(request, "foodie_app/add_category.html", context)
    else:
        form = CategoryForm()
        context = {"form": form}
        return render(request, "foodie_app/add_category.html", context)
    
# def add_recipe(request):
#     if(request.method == "POST"):
#         form = RecipeForm(request.POST)
#         if(form.is_valid()):
#             form.save()
#             return redirect("recipes:recipe_index")
#     else:
#         form = RecipeForm()
#     return render(request, "foodie_app/add_recipe.html", {"form": form}) 

# Adding a recipe when we already are inside a specific category or adding one from the home page link.
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
    return render(request, "foodie_app/add_recipe.html", context=context)