from django.db import models

from recipes.models import Recipe

# Create your models here.
# Each Recipe can have ZERO to MANY comments.

class Comment(models.Model):
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    # Everytime a Recipe gets deleted, its comments always get deleted!

    def __str__(self):
        return self.text
