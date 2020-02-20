from django import forms
from .models import Rate

class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ['subject', 'professor', 'title', 'content', 'rate']