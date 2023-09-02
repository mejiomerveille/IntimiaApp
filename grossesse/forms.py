from django import forms
from .models import Grossesse

class GrossesseForm(forms.ModelForm):
    
    class Meta:
        model = Grossesse
        fields = ['start_date']