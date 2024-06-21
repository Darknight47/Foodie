
from django import forms

choices = [
    ('happy', 'Happy'),
    ('neutral', 'Neutral'),
    ('sad', 'Sad')
]

# The generic form of FORM class for customization
class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    feedback = forms.CharField()
    satisfaction = forms.ChoiceField(choices=choices)