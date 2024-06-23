from django.urls import path
from . import views # Importing views from the current directory

app_name = "foodie_app"
urlpatterns = [
    path("", views.index, name="index"),
    path("recipes/<int:category_id>/", views.catRecipes, name="cat_recipes"),
    path("addCategory/", views.add_category, name="add_category"),
    path("add-recipe/", views.add_recipe, name="add_recipe_in_general"),
    path("add-recipe/category/<int:category_id>/", views.add_recipe, name="add_recipe_with_cat")

]
