from django.urls import path
from . import views

# A namespace
app_name = "sandbox"

urlpatterns = [
    # when we go to the "" (url address/path), we are going to serve the helloWorld() function.
    path("", views.helloWorld),   
    path("index", views.index) 
]
