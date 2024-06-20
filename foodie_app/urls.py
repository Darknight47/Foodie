from django.urls import path
from . import views # Importing views from the current directory

app_name = "foodie_app"
urlpatterns = [
    path("", views.index, name="index"),
    path("recipes/<int:category_id>/", views.catRecipes, name="cat_recipes")
]
