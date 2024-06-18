from django.db import models

# Create your models here.
# A category can have one or many categories.
class Category(models.Model):
    name = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=True)  # Capture the date & time when this category added
    
    def __str__(self):
        return self.name