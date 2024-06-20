from django.db import models

# Create your models here.
# A category can have one or many categories.
class Category(models.Model):
    name = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=True)  # Capture the date & time when this category added
    
    # Changing or specifying information about this model.
    # Specyfing Meta Options.
    class Meta: 
        ordering = ["-name"] # For descending order of the name property. "name" for ascending ordering.
        #ordering = ["name", "date_added"] # Ordering by two properties.
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name