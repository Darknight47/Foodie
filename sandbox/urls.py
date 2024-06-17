from django.urls import path
from . import views

# A namespace
app_name = "sandbox"

urlpatterns = [
    # when we go to the "" (url address/path), we are going to serve the helloWorld() function.
    path("", views.helloWorld),   
    # When we go to the sandbox/ then we need to add "index" to make it "sandbox/index" to execute sandbox.index
    path("index", views.index) 
]
