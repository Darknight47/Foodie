from django.contrib import admin
from . models import Category, Recipe

# A class for customizing the fields that we are seeing in the UI.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "date_added")
    search_fields = ["name"] # Able to search by name

class RecipeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "date_added")

# Register your models here.
# registering the customization to the model.
admin.site.register(Category, CategoryAdmin)

# registering the recipe model
admin.site.register(Recipe, RecipeAdmin)