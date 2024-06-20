from django.urls import path
from . import views

app_names = "recipe"
urlpatterns = [
    path("", views.index),
    path("recipe/<int:recipe_id>", views.recipe)
]
