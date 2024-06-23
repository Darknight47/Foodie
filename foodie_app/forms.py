
from django import forms

from foodie_app.models import Category
from recipes.models import Recipe


# A form for creating Category from UI.
class CategoryForm(forms.ModelForm):
    class Meta: #Defining meta data about this form
            # We need to attach this category form to a model.
            model = Category
            fields = ["name"] #User only need to write the name of a category for creating one.
            labels = {
                  'name': 'Category Name'
            }
            widgets ={
                  "name": forms.TextInput(attrs={"placeholder": "Category Name"})
            }

class RecipeForm(forms.ModelForm):
      class Meta:
            model = Recipe
            fields = ["name", "description", "ingredients", "directions", "category"]
            widgets = {
                  "name": forms.TextInput(attrs={"placeholder": "Your Name", "class": "recipe_name"}),
                  "description": forms.Textarea(attrs={"placeholder": "Description of the recipe", "class": "recipe_desc"}),
            }
