
from django import forms

from foodie_app.models import Category


# A form for creating Category from UI.
class CategoryForm(forms.ModelForm):
    class Meta: #Defining meta data about this form
            # We need to attach this category form to a model.
            model = Category
            fields = ["name"] #User only need to write the name of a category for creating one.
            labels = {
                  'name': 'Category Name'
            }