from django import forms
from .models import Symptome

class SymptomeForm(forms.ModelForm):
    class Meta:
        model = Symptome
        fields = ['nom','intensite', 'description']