from django import forms
from .models import Project

#Creating form class
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields ="__all__"