from django.db import models

from foodie_app.models import Category

# Create your models here.
# Relationship between Recipe and Category is ONE to MANY.

# Recipe Model
# Each recipe belongs to one category.
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    ingredients = models.TextField()
    directions = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Everytime we delete a category, all the recipes belong to that category deletes as well!

    def __str__(self):
        return self.name