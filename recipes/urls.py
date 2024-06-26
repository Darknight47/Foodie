from django.urls import path
from . import views

app_name = "recipes"
urlpatterns = [
    path("", views.index, name="recipe_index"),
    path("<int:recipe_id>", views.recipeView, name="recipe_detail") #recipe/id
]
