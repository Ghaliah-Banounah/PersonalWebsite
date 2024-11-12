from django import forms
from .models import Interest

#Creating form class
class InterestForm(forms.ModelForm):
    class Meta:
        model = Interest
        fields ="__all__"