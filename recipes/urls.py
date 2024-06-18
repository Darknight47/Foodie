from django.urls import path
from . import views

app_names = "recipe"
urlpatterns = [
    path("", views.index)
]
