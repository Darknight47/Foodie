from django.urls import path
from . import views

app_names = "recipes"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:recipe_id>", views.recipeView, name="recipe_detail") #recipe/id
]
