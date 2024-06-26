"""
URL configuration for foodie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # After creating the first function and path in the first app, we are updating now the project about the changes in the app.
    # "appName/"
    # Url to the foodie_app
    path("", include("foodie_app.urls")),
    # Url to the sandbox app
    path( "sandbox/", include("sandbox.urls")),
    # Url to the Recipes
    path("recipes/", include("recipes.urls")),
    # Url to the Comments
    path("comments/", include("comments.urls"))
]
