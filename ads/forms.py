from django import forms
from .models import Ads

class Adform(forms.ModelForm):
    class Meta:
        model = Ads
        fields = ['title', 'description']