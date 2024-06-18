from django.contrib import admin

from recipes.models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "date_added")

# Register your models here.
# registering the recipe model
admin.site.register(Recipe, RecipeAdmin)