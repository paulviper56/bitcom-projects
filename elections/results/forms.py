from django import forms
from .models import Electionresult

class ElectionResultForm(forms.ModelForm):
    class Meta:
        model = Electionresult
        fields = ['party', 'polling_unit', 'votes']
        widgets = {
            'party': forms.Select(attrs={'class': 'form-control'}),
            'polling_unit': forms.Select(attrs={'class': 'form-control'}),
            'votes': forms.NumberInput(attrs={'class': 'form-control'}),
        }
