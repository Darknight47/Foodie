from django.urls import path
from . import views

app_names = "recipe"
urlpatterns = [
    path("", views.index),
    path("<int:recipe_id>", views.recipe) #recipe/id
]
