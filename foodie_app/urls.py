from django.urls import path
from . import views # Importing views from the current directory

app_name = "foodie"
urlpatterns = [
    path("", views.index, "index")
]
