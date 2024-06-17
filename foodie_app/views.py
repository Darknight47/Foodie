from django.shortcuts import render

# Create your views here.
def index(request):
    #Inside the foodie_app execute the index.html
    return render(request, "foodie_app/index.html")