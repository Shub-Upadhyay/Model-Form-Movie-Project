from django import forms
from .models import Movies
class Movies_form(forms.ModelForm):
    class Meta:
        model = Movies
        fields  = '__all__'