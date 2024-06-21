
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
    satisfaction = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)

    # Validating the email input.
    def clean_email(self):
        emailInput = self.cleaned_data['email'] 
        if("@gmail.com" not in emailInput):
            raise forms.ValidationError("Please Your Gmail")
        return emailInput